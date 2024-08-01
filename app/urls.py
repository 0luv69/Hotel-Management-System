from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotels/', views.hotels, name='hotel'),
    path('hotel/<int:pk>/', views.hotel_detail,name='hotelPage'),
]

