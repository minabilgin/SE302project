from django.contrib import admin
from .models import Clubs
from .models import Events
from .models import FavoriteClubs
from .models import Comments

# Register your models here.

admin.site.register(Clubs)
admin.site.register(Events)
admin.site.register(FavoriteClubs)
admin.site.register(Comments)

