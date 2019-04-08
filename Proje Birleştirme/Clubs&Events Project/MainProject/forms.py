from django import forms
from .models import Clubs
from .models import Events


class ClubForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = ('club_name', 'club_infos', 'club_emblem')


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('club', 'event_name', 'event_created_date', 'event_day', 'event_location', 'event_info')
