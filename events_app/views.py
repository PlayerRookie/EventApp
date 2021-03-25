from django.shortcuts import render
from django.http import HttpResponse 
from events_app.forms import UserForm, AboutForm, GoalForm, EventCreationForm
from events_app.models import EventUsers, AboutUser, UserGoals, Events
import events_app.event_loader as eLoader
from datetime import datetime
from django.shortcuts import redirect
from django.urls import reverse

# generate some constants
APP_NAME = 'Events'
MOST_POP_EVENTS_COUNT = 3


# session constants
SESSION_TIMEOUT = 15 # 15 minutes

SESSION_EMAIL = 'email'
SESSION_LOGIN_TIME = 'login_time'
SESSION_USER_NAME = 'name'
# Create your views here.

"""
This will use the base.html template, along with th index.html files
to generte the view
"""
def index(request):
    context = {'app_name': APP_NAME, 'pop_events':eLoader.get_most_popular()}
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
    if is_logged_in(request):
        return redirect(reverse('events_app:profile'))
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # validate then show profile
        if authenticate(request, email, password):
            return redirect(reverse('events_app:profile'))
    return render(request, "event_templates/login.html")

def profile(request):
    if not is_logged_in(request):
        return redirect(reverse('events_app:login'))
    
    # get all the users with this email
    users = EventUsers.objects.filter(mail=request.session[SESSION_EMAIL])
    # if not one, means more users with same info or no users, either way block it
    if not len(users) == 1:
        clear_session(request)
        return redirect(reverse('events_app:login'))
    
    user = users[0]
    user_about = AboutUser.objects.filter(user=user)[0]
    user_goals = UserGoals.objects.filter(user=user)[0]
    
    user_context_general = {'Name': user.name, 'Email': user.mail, 'Date Of Birth':user_about.dob, 'Gender':AboutUser.gender_from_id(user_about.gender)}
    user_context_goals = [user_goals.goal_1,user_goals.goal_2, user_goals.goal_3]
    
    context = {'General': user_context_general, 'Goals': user_context_goals, 'Biography':user_goals.bio}
    
    
    return render(request, "event_templates/profile.html", context)


def register(request):
    if is_logged_in(request):
        return redirect(reverse('events_app:profile'))
    
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

def add_event(request):
    if not is_logged_in(request):
        return redirect(reverse('events_app:login'))
    
    if request.method == 'POST':
        add_form = EventCreationForm(request.POST, request.FILES)
        
        if add_form.is_valid():
            event = add_form.save(commit=False)
            event.creator =  get_user_from_session(request)
            event.save()
            return render(request, "event_templates/added.html")
        else:
            print(add_form.errors)
    else:
        add_form = EventCreationForm()
        
    context = {'app_name': APP_NAME, 'form':add_form}
    return render(request, "event_templates/add_event.html", context)
        
"""
Authenticates login

returns True if valid, false if Not

starts session, sets session timeout
"""
def authenticate(request, email, password):
    # clear the session before allowing another login
    clear_session(request)
    
    objects = EventUsers.objects.filter(mail=email, password=password)
    if len(objects) == 0:
        return False
    
    request.session[SESSION_EMAIL] = email
    request.session[SESSION_LOGIN_TIME] = str(datetime.now())
    request.session[SESSION_USER_NAME] = objects[0].name
    return True

"""
Clears the session indicating a logout

"""
def clear_session(request):
    vals = [SESSION_EMAIL, SESSION_TIMEOUT, SESSION_USER_NAME]
    
    for val in vals:
        if in_session(request, val):
            request.session.pop(val)

"""
Checks if a session is valid for a logged in user
If session times out, logs out and clears session

If session didn't time out, resets the session timer.
"""
def is_logged_in(request):
    if not in_session(request):
        return False
    
    elapsed = get_session_elapsed(request)
    print("IN SESSION",elapsed)
    if elapsed == -1 or elapsed > SESSION_TIMEOUT:
        clear_session(request)
        return False
    request.session[SESSION_LOGIN_TIME] = str(datetime.now())
    return True

# returns the elapsed time in minutes
def get_session_elapsed(request):
    if not SESSION_LOGIN_TIME in request.session:
        return -1
    start_time_str = request.session[SESSION_LOGIN_TIME]
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S.%f")
    
    return int((datetime.now()-start_time).seconds/60)
    
def in_session(request, value=SESSION_EMAIL):
    return value in request.session

def get_user_from_session(request):
    if not is_logged_in(request):
        return None
    user = EventUsers.objects.filter(mail=request.session[SESSION_EMAIL])[0]
    print("USER IS:", user)
    return user
    