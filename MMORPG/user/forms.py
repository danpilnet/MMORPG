from django.forms import ModelForm
from django.contrib.auth import get_user_model

from post.models import Post


class RegistrationForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
