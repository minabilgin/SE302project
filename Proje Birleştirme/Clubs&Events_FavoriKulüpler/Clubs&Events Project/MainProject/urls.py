from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('kulupler', views.page1, name='kulupler'),
                  path('Login', views.page4, name='Login'),
                  path('Register', views.page5, name='Register'),
                  path('KulupDetail/<str:pk>/', views.club_details, name='KulupDetay'),
                  path('ModeratorPanel', views.page6, name='ModeratorPanel'),
                  path('', views.anasayfa, name='anasayfa'),
                  path('changeUserStatus', views.changeUserStatus, name='changeUserStatus'),
                  path('new_club', views.addclub, name='new_club'),
                  path('edit_club', views.page7, name='edit_club'),
                  path('edit_club_detail/<str:pk>/', views.editclub, name='edit_club_detail'),
                  path('new_event', views.addevent, name='new_event'),
                  path('edit_event', views.page9, name='edit_event'),
                  path('edit_event_detail/<str:pk>/', views.editevent, name='edit_event_detail'),
                  path('add_comment/<str:pk>/', views.adding_comment, name='add_comment'),
                  path('allcomments', views.allcomments, name='allcomments'),
                  path('changeUserStatus', views.allcomments, name='changeUserStatus'),
                  path('allcommentsdetail/<int:pk>/', views.allcomments_details, name='allcommentsdetails'),
                  path('edit_club_detail/<str: pk>/change', views.change_club_status, name="change_status"),
                  path('EventDetail/<int:pk>/', views.event_detail, name='EventDetail'),
                  path('logout', views.user_logout, name="user_logout"),
                  path('commentstatus/<str:pk>/', views.change_comment_status, name='commentstatus'),
                  path('favorite_clubs', views.page3, name='favorite_clubs'),
                  path('add_favorite_clubs', views.add_favorite_clubs, name='add_favorite_clubs'),
                  path('remove_favorite_clubs', views.remove_favorite_clubs, name='remove_favorite_clubs'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
