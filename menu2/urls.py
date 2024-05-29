from django.urls import path, re_path
from . import views

urlpatterns= [
    path('', views.arm),
    path('arm/', views.arm),
    path('back/', views.back),
    path('chest/', views.chest),
    path('legs/', views.legs),
    path('shoulder/', views.shoulder),
    path('aerobic/', views.aerobic),
]