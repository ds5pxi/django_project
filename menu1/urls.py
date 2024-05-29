from django.urls import path, re_path
from . import views

urlpatterns= [
    path('', views.index),
    path('/', views.index),
    path('views/', views.views),
    path('views/edit/', views.edit),
    path('write/', views.write),

]