from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Clubs(models.Model):
    club_name = models.CharField(max_length=250, primary_key=True)
    club_infos = models.CharField(max_length=2500)
    club_emblem = models.ImageField(upload_to='uniqueEmblem')

    def __str__(self):
        return self.club_name


class Events(models.Model):
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    event_created_date = models.DateTimeField(default=timezone.now)
    event_day = models.DateTimeField(blank=True, null=True)
    event_location = models.CharField(max_length=250)
    event_info = models.CharField(max_length=2500, null=True)

    def publish(self):
        self.event_created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name


class FavoriteClubs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)


class Comments(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False)

