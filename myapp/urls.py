from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', views.insert),
    path('', views.home),
    path('show/', views.show),
    
]
