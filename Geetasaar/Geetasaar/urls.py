from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',admin.site.urls),
    path('',views.demo),
    path('Contact Us/',views.Contact),
    path('history/',views.history),
    path('Teachings/',views.Teachings),
    path('Images/',views.Images)]
    
