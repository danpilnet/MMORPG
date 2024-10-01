from django.urls import path
from .views import Registration, access_registration, Authentication, log_out, MyProfile


urlpatterns = [
    path('registration/', Registration.as_view()),
    path('access/', access_registration),
    path('authentication/', Authentication.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('myprofile/<int:pk>/', MyProfile.as_view()),
]