from django.contrib import admin
from django.urls import path
from empresa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departamento/', views.departamento_list, name='departamento'),
    path('departamento/<int:pk>', views.departamento_detail, name='departamento'),
    path('projeto/',views.projeto_list, name='projeto'),
    path('projeto/<int:pk>', views.projeto_detail, name='projeto'),
    path('funcionarios/',views.funcionario_list, name='funcionarios'),
    path('funcionarios/<int:pk>',views.funcionario_detail, name='funcionarios'),

]
