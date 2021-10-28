from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from empresa import views

router = routers.DefaultRouter()

router.register(r'departamento', views.DepartamentoView, basename='departamento')
router.register(r'projeto', views.ProjetoView, basename='projetos')
router.register(r'funcionarios',views.Funcionarios, basename='funcionarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework'))

]
