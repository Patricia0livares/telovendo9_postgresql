"""bootstrap_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blogapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
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

urlpatterns += staticfiles_urlpatterns()
