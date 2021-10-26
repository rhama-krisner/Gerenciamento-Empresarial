from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from empresa import views

router = routers.DefaultRouter()

router.register(r'departamento', views.DepartamentoView)
router.register(r'projeto', views.ProjetoView)
router.register(r'funcionarios',views.Funcionarios)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
