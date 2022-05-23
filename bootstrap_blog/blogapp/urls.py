from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('proveedor/', views.ingresoproveedor, name='proveedor'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('mensajes/', views.mensaje_cliente, name='mensajes'),
    path('ingreso_mensaje/', views.ingreso_mensaje, name='ingreso_mensaje'),
    path('mensaje_edit/<int:pk>',views.mensaje_edit, name='mensaje_edit'),
    path('mensaje_delete/<int:pk>',views.mensaje_delete, name='mensaje_delete'),
]