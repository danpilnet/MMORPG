from django.urls import path
from .views import Responses

urlpatterns = [
    path('respons/', Responses.as_view())
]