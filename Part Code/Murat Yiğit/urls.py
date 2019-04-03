from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  
                  path('Login', views.page4, name='Login'),
                  path('Register', views.page5, name='Register'),
                  path('', views.anasayfa, name='anasayfa'),
                  path('add_comment/<str:pk>/', views.adding_comment, name='add_comment'),
                  path('allcomments', views.allcomments, name='allcomments'),
                  path('allcommentsdetail/<int:pk>/', views.allcomments_details, name='allcommentsdetails'),
                  path('logout', views.user_logout, name="user_logout"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
