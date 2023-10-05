from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:rooms>/', views.rooms, name='rooms'),
    path('check', views.check, name='check'),
    path('send', views.send, name='send'),
]