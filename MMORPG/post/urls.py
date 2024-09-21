from django.urls import path
from .views import PostCreate, PostList


urlpatterns = [
    path('postcreate/', PostCreate.as_view()),
    path('post/', PostList.as_view())
]