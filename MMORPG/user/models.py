from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    image = models.ImageField(null=True, blank=True, verbose_name='Image')
    accessed = models.BooleanField(default=False)
    email = models.EmailField(unique=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()
