from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from manutencao import views
from manutencao.views import CompanyViewSet

router = routers.DefaultRouter()

router.register('companies', CompanyViewSet, basename="Companies")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load', views.testview),
    path('home', views.homeview),
    path('',include(router.urls))
]
