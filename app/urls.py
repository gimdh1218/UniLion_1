from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('introduce', views.introduce, name='introduce'),
    path('story', views.story, name='story'),
    path('community', views.community, name='community'),
    path('question', views.question, name='question'),
]