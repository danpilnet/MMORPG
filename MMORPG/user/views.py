from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm
from post.models import Post



User = get_user_model()

class Registration(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        subject = 'Test'

        data = request.POST
        email = data['email']
        password = data['password']

        html_content = f'<a href="http://127.0.0.1:8000/access/?email={email}">Подтвердить</a>'
        message = EmailMultiAlternatives(subject=subject, to=['dnpdnp28@gmail.com', ])
        message.attach_alternative(html_content,mimetype='text/html')
        message.send()

        user = User.objects.create(email=email)
        user.set_password(password)
        user.save()

        return HttpResponseRedirect('/registration')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RegistrationForm()
        context['form'] = form
        context['profile'] = not self.request.user.is_authenticated
        context['form_email'] = self.request.user.email if not self.request.user.is_anonymous else False
        return context

def access_registration(request):

    email = request.GET['email']

    user = User.objects.get(email=email)
    user.accessed = True
    user.save()

    return HttpResponseRedirect('/registration')

class Authentication(TemplateView):
    template_name = 'authentication.html'

    def post(self,request):

        data = request.POST
        email = data['email']
        password = data['password']

        user = authenticate(request,email=email,password=password)
        login(request,user)
        return HttpResponseRedirect('/post')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/registration')


class MyProfile(DetailView, LoginRequiredMixin):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'myprofile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_email'] = self.request.user.email
        context['posts'] = Post.objects.filter(user_id=self.request.user.pk)
        return context

    def get_queryset(self):
        return get_user_model().objects.filter(pk=self.request.user.pk)
