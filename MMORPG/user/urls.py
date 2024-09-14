from django.urls import path
from .views import Registration, access_registration


urlpatterns = [
    path('registration/', Registration.as_view()),
    path('access/', access_registration)
]