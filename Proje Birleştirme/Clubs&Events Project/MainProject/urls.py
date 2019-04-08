from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path('kulupler', views.page1, name='kulupler'),
                  path('Favori Kulüpler', views.page3, name='Favori Kulüpler'),
                  path('Login', views.page4, name='Login'),
                  path('Register', views.page5, name='Register'),
                  path('KulupDetail/<str:pk>/', views.club_details, name='KulupDetay'),
                  path('ModeratorPanel', views.page6, name='ModeratorPanel'),
                  path('', views.anasayfa, name='anasayfa'),
                  path('add_comment/<str:pk>/', views.adding_comment, name='add_comment'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
