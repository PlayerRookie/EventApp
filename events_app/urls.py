from django.urls import path
from events_app import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'events_app'



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('events', views.events, name='events'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('add_event', views.add_event, name='add_event'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)