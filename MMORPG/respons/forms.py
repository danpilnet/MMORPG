from django.forms import ModelForm
from .models import Response


class FormRespons(ModelForm):

    class Meta:
        model = Response
        fields = ['text',]
