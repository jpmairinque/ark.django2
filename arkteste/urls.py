from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from manutencao import views
from manutencao.views import CompanyViewSet, EquipmentViewSet, CompanyEquipmentsViewSet, ChamadoViewSet, EquipmentChamadosViewSet

router = routers.DefaultRouter()

router.register('companies', CompanyViewSet, basename="Companies")
router.register('equipments', EquipmentViewSet, basename="Equipments")
router.register('chamados', ChamadoViewSet, basename="Chamados")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load', views.testview),
    path('home', views.homeview),
    path('',include(router.urls)),
    path('companies/<int:pk>/equipments/', CompanyEquipmentsViewSet.as_view()),
    path('equipments/<int:pk>/chamados/', EquipmentChamadosViewSet.as_view()),
]
