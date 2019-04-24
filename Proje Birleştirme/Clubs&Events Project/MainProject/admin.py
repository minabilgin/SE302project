from django.contrib import admin
from .models import Clubs
from .models import Events
from .models import Comments


# Register your models here.

def make_publish(modeladmin, request, queryset):
    queryset.update(status='P')
    make_publish.short_description = "Mark selected comments as publisted"


def make_reject(modeladmin, request, queryset):
    queryset.update(status='R')
    make_reject.short_description = "Mark selected comments as rejected"


def make_draw(modeladmin, request, queryset):
    queryset.update(status='D')
    make_draw.short_description = "Mark selected clubs as draw"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'status']
    ordering = ['comment']
    actions = [make_publish, make_reject]


class ClubAdmin(admin.ModelAdmin):
    list_display = ['club_name', 'status']
    ordering = ['club_name']
    actions = [make_draw]


admin.site.register(Clubs, ClubAdmin)
admin.site.register(Events)
admin.site.register(Comments, CommentAdmin)
