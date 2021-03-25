import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'events.settings')

import django
django.setup()

import random as random

from events_app.models import EventUsers, AboutUser, UserGoals, Events, EventParticipation

from django.db.models import Count, F


def populate():
    user_names = ['Jad', 'Ahmad', 'Fatma', 'Ali', 'Mariam', 'Karma', 'Aya']
    users = []
    for name in user_names:
        user = add_user(name, name+"@email.com",name+"123")
        set_goals_and_bio(user, "My First goal " + name, name + " My Second goal", name + " my third goal", name + " my biooo")
        set_about(user, '1998-05-23', 'F', 'S', 'S')
        users.append(user)
    
    events = [('Football', 'S', 'SCOT'), ('Basketball', 'S', 'LOND'), ('Boat Ride', 'F', 'LOND'), ('Party', 'F', 'WALE')]
    
    for data in events:
        # not to create duplicate events, since they have random users
        if len(Events.objects.filter(name=data[0])) > 0:
            continue
        event = add_event(data[0], data[1], 'event_images/football.jpeg', data[2], random.choice(users))
        for i in range(int(random.random()*4)):
            add_participation(event, random.choice(users)).save()
        

def add_user(name, email, password):
    user = EventUsers.objects.get_or_create(name=name,mail=email,password=password)[0]
    user.save()
    return user

def set_goals_and_bio(user, goal1, goal2, goal3, bio):
    goals = UserGoals.objects.get_or_create(user=user, goal_1=goal1,goal_2=goal2,goal_3=goal3, bio=bio)[0]
    
    goals.save()
    return goals

def set_about(user, dob, gender, status, occupation):
    about =AboutUser.objects.get_or_create(user=user,dob=dob,gender=gender,status=status,occupation=occupation)[0]
    about.save()
    return about
    
def add_event(name, category, image, location, creator):
    event = Events.objects.get_or_create(name=name, category=category,image=image,location=location,creator=creator)[0]
    event.save()
    return event

def add_participation(event, user):
    part = EventParticipation.objects.get_or_create(event=event, user=user)[0]
    return part

def get_most_popular(limit=3):
    events = Events.objects.annotate(count=Count('eventparticipation'), creator_name=F('creator__name')).order_by('count')

    
    lst = events.values_list('name', 'category', 'count', 'image', 'creator_name').reverse()[0:limit]
    return lst
    
if __name__ == '__main__':
    print('Starting events population script...')
    populate()
    print(get_most_popular())
    

    
    