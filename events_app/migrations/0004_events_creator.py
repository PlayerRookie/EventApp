# Generated by Django 3.1.7 on 2021-03-24 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0003_events_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='creator',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='events_app.eventusers'),
            preserve_default=False,
        ),
    ]
