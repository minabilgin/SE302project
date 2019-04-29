from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS_CHOICES = (  # comments
    ('A', 'Accepted'),
    ('W', 'Waiting'),
    ('R', 'Rejected'),
)

STATUS_CHOICES2 = (  # clubs
    ('P', 'Published'),
    ('D', 'Draw'),
)


class Clubs(models.Model):
    club_name = models.CharField(max_length=250, primary_key=True)
    club_infos = models.CharField(max_length=2500)
    club_emblem = models.ImageField(upload_to='uniqueEmblem')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES2, default='P')

    def __str__(self):
        return self.club_name


class Events(models.Model):
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    event_created_date = models.DateTimeField(default=timezone.now)
    event_day = models.DateTimeField(blank=True, null=True)
    event_location = models.CharField(max_length=250)
    event_info = models.CharField(max_length=2500, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES2, default='P')

    def publish(self):
        self.event_created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name


class Comments(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='W')
    created_day = models.DateTimeField(default=timezone.now)


def make_published(modeladmin, request, queryset):
    queryset.update(status='Published')
    make_published.short_description = "Mark selected comments as published"


def make_rejected(modeladmin, request, queryset):
    queryset.update(status='Rejected')
    make_rejected.short_description = "Mark selected comments as Rejected"


def make_draw(modeladmin, request, queryset):
    queryset.update(status='Draw')
    make_draw.short_description = "Mark selected as Draw"
