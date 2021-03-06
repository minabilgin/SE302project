# Generated by Django 2.1.7 on 2019-04-25 15:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('club_name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('club_infos', models.CharField(max_length=2500)),
                ('club_emblem', models.ImageField(upload_to='uniqueEmblem')),
                ('status', models.CharField(choices=[('P', 'Published'), ('D', 'Draw')], default='P', max_length=1)),
                ('favorite_user', models.ManyToManyField(related_name='favorite_clubs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('status', models.CharField(choices=[('A', 'Accepted'), ('W', 'Waiting'), ('R', 'Rejected')], default='W', max_length=1)),
                ('created_day', models.DateField(default=datetime.datetime(2019, 4, 25, 15, 58, 16, 214922, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_day', models.DateTimeField(blank=True, null=True)),
                ('event_location', models.CharField(max_length=250)),
                ('event_info', models.CharField(max_length=2500, null=True)),
                ('status', models.CharField(choices=[('P', 'Published'), ('D', 'Draw')], default='P', max_length=1)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainProject.Clubs')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainProject.Events'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
