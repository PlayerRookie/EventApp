# Generated by Django 3.1.7 on 2021-03-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0002_eventparticipation_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='category',
            field=models.CharField(choices=[('S', 'SPORTS'), ('F', 'FUN'), ('O', 'Other')], default=('S', 'SPORTS'), max_length=3),
        ),
    ]
