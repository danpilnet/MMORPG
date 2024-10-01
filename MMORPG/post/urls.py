from django.urls import path
from .views import PostCreate, PostList, PostUpdate, PostDetail, PostDelete


urlpatterns = [
    path('post/create/', PostCreate.as_view()),
    path('post/', PostList.as_view()),
    path('post/<int:pk>/update/', PostUpdate.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('post/<int:pk>/delete/', PostDelete.as_view()),
]