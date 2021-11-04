from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from empresa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departamento/', views.departamento_list),
    path('departamento/<int:pk>', views.departamento_detail),
    path('projeto/',views.projeto_list),
    path('projeto/<int:pk>', views.projeto_detail),
    path('funcionarios/',views.funcionario_list, name='funcionarios'),
    path('funcionarios/<int:pk>',views.funcionario_detail, name='funcionarios_detail'),

]
