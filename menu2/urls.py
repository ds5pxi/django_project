from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('/menu/index/', views.index),
    path('video/', views.video, name='V'),
    path('video/aerobic/', views.aerobic, name='AB'),
    path('video/arm/', views.arm, name='A'),
    path('back/', views.back, name='B'),
    path('chest/', views.chest, name='C'),
    path('leg/', views.leg, name='L'),
    path('shoulder/', views.shoulder, name='S'),
    path('add/', views.add, name='AD'),
]