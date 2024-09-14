from django.shortcuts import render
from .forms import RegistrationForm
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model


class Registration(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        subject = 'Test'
        html_content = '<a href="http://127.0.0.1:8000/access/">Подтвердить</a>'
        message = EmailMultiAlternatives(subject=subject, to=['dnpdnp28@gmail.com', ])
        message.attach_alternative(html_content,mimetype='text/html')
        message.send()
        data = request.POST
        print(data['email'])
        a = data['email']
        b = data['password']
        user_registration = get_user_model().objects.create(email=a, password=b)
        return HttpResponse('Hello')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RegistrationForm()
        context['form'] = form
        return context

def access_registration(request):
    