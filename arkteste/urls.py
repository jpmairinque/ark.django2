from rest_framework import routers
from django.contrib import admin
from django.urls import path
from manutencao import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load', views.testview),
    path('home', views.homeview),
]
