# Generated by Django 2.1.3 on 2018-12-19 18:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('club_name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('club_infos', models.CharField(max_length=2500)),
                ('club_emblem', models.ImageField(blank=True, upload_to='uniqueEmblem')),
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
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainProject.Clubs')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainProject.Clubs')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='favoriteclubs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainProject.Users'),
        ),
    ]
