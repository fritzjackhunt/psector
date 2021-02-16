from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='homepage'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('news', views.news, name='news'),
    path('contacts', views.contacts, name='contacts'),
    path('events', views.events, name='events'),
]