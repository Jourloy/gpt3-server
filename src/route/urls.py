from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('text', views.gpt3, name='text'),
    path('title', views.title, name='title'),
    path('image', views.image, name='image')
]
