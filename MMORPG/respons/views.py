from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives

from .models import Response
from .filters import ResponsFilter


class Responses(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'respons.html'
    context_object_name = 'respons'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_email'] = self.request.user.email
        context['filterset'] = self.filterset
        context['user_response'] = Response.objects.filter(post_id__user_id=self.request.user.pk)
        return context

    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        Response.objects.get(pk=int(pk)).delete()

        return HttpResponseRedirect('#')
