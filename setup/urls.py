from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from empresa import views

router = routers.DefaultRouter()

router.register(r'funcionarios', views.Funcionarios)
router.register(r'projeto', views.Projeto)
router.register(r'departamento', views.Departamento)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
