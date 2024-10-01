from django.shortcuts import render
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives

from .models import Post
from respons. forms import FormRespons
from respons. models import Response


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'postcreate.html'
    form_class = PostForm
    success_url = '/post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_email'] = self.request.user.email
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()

        return super().form_valid(form)


class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = not self.request.user.is_authenticated
        context['form_email'] = self.request.user.email if not self.request.user.is_anonymous else False
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'postupdate.html'
    context_object_name = 'update'
    success_url = '/post'

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = not self.request.user.is_authenticated
        context['form_email'] = self.request.user.email
        return context

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'postdetail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_email'] = self.request.user.email
        context['respons'] = FormRespons
        return context

    def post(self, request, *args, **kwargs):
        user_id = request.user.pk
        text = request.POST['text']
        post_id = kwargs['pk']
        comment = Response.objects.create(user_id=user_id, text=text, post_id=post_id)
        post = Post.objects.get(pk=post_id)
        content = '<h1>На ваш пост отклик</h1>'

        message = EmailMultiAlternatives(to=[post.user.email, ], subject='Отклик')
        message.attach_alternative(content=content, mimetype='text/html')
        message.send()

        return HttpResponseRedirect(f'/post/{post_id}/')


class PostDelete(DeleteView):
    model = Post
    template_name = 'postdelete.html'
    context_object_name = 'delete'
    success_url = '/post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_email'] = self.request.user.email
        return context

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.pk)