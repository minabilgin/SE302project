from django import forms
from .models import Clubs, Events, Comments
from django.utils import timezone
from django.core.exceptions import ValidationError


class ClubForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = ('club_name', 'club_infos', 'club_emblem', 'status')


class UpdateEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateEventForm, self).__init__(*args, **kwargs)
        self.fields['event_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Event Name'})
        self.fields['event_day'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Day'})
        self.fields['event_location'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Location'})
        self.fields['event_info'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Informations'})

    class Meta:
        model = Events
        fields = (
            'event_name',
            'event_day',
            'event_location',
            'event_info'
        )

    def save(self, commit=True):
        event = super(UpdateEventForm, self).save(commit=False)
        if commit:
            event.save()
        return event

    def clean_event_day(self):
        date = self.cleaned_data['event_day']

        if date < timezone.now():
            raise ValidationError('Eski Tarihli Bir Etkinlik Açamazsınız!')
        return date


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['event_created_date'].widget.attrs['readonly'] = True

    def clean_event_day(self):
        date = self.cleaned_data['event_day']

        if date < timezone.now():
            raise ValidationError('Eski Tarihli Bir Etkinlik Açamazsınız!')
        return date

    class Meta:
        model = Events
        fields = ('club', 'event_name', 'event_created_date', 'event_day', 'event_location', 'event_info', 'status')
        readonly_fields = ['club']


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['event'].widget.attrs['readonly'] = True
        self.fields['user'].widget.attrs['readonly'] = True
        self.fields['comment'].widget.attrs['readonly'] = True

    class Meta:
        model = Comments
        fields = ('event', 'user', 'comment', 'status')
