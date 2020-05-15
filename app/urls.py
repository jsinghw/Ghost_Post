from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('submission/', views.submission),
    path('upvote/<int:post_id>', views.upvote),
    path('downvote/<int:post_id>', views.downvote)
]
