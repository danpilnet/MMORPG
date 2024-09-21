from django.shortcuts import render
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Post

class PostCreate(CreateView):
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
    paginate_by = 5

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile'] = not self.request.user.is_authenticated
    #     context['form_email'] = self.request.user.email if not self.request.user.is_anonymous else False
    #     return context