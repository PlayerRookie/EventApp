from events_app.models import EventUsers, AboutUser, UserGoals, Events, EventParticipation
from django.db.models import Count, F


def get_most_popular(limit=3):
    events = Events.objects.annotate(count=Count('eventparticipation'), creator_name=F('creator__name')).order_by('count')

    
    lst = events.values_list('name', 'category', 'count', 'image', 'creator_name').reverse()[0:limit]
    return lst

