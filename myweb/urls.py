"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path("", include('menu2.urls')),
=======
    path("", views.index),
    path('account/login/', views.login),
    path('account/logout/', views.logout),
    path('account/register/', views.createAccount),
    path('account/myinfo/', views.myinfo),
    path('account/myinfoDel/', views.myinfoDel),
>>>>>>> 2bd7fcd493affb054228f38b4632234a9d153bf3
]
