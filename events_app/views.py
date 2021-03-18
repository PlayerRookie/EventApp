from django.shortcuts import render
from django.http import HttpResponse 
from events_app.forms import UserForm, AboutForm, GoalForm
from events_app.models import EventUsers
from datetime import datetime
# generate some constants
APP_NAME = 'Events'
MOST_POP_EVENTS_COUNT = 3

# Create your views here.

"""
This will use the base.html template, along with th index.html files
to generte the view
"""
def index(request):
    context = {'app_name': APP_NAME, 'pop_event_count':range(MOST_POP_EVENTS_COUNT)}
    return render(request, "event_templates/index.html", context)
    
def about(request):
    context = {'app_name': APP_NAME}
    return render(request, "event_templates/about.html", context)

def events(request):
    x = range(3)
    context = {'app_name': APP_NAME, 
               'categories': {'Most Populer Events': x, 'New Events Near You': x, 'Events By Category': x}}
    return render(request, "event_templates/events.html", context)
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        objects = EventUsers.objects.filter(mail=email, password=password)
        if len(objects)>0:
            return profile(request)
    return render(request, "event_templates/login.html")

def profile(request):
    
    info = {'name':'Test'}
    context = {'user_info': info}
    return render(request, "event_templates/profile.html")


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        about_form = AboutForm(request.POST)
        goal_form = GoalForm(request.POST)
        if user_form.is_valid() and about_form.is_valid() and goal_form.is_valid():
            user = user_form.save()
            user.save()
            
            print("User saved!")
            about_form.user = user
            about_form.save()
            print("About Failed to save")
            goal_form.user = user
            goal_form.save()
            return render(request, "event_templates/registered.html")
        else:
            print(user_form.errors, about_form.errors, goal_form.errors)
    else:
        user_form = UserForm()
        about_form = AboutForm()
        goal_form = GoalForm()
    
    context = {'app_name': APP_NAME, 'user_form':user_form, 'about_form': about_form, 'goal_form': goal_form}
    return render(request, "event_templates/register.html", context)


    