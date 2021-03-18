from django.urls import path
from events_app import views

app_name = 'events_app'



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('events', views.events, name='events'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile', views.login, name='profile'),
]