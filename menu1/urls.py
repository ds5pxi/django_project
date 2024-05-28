from django.urls import path, re_path
from . import views

urlpatterns= [
    path('', views.index),
    path('index/', views.index),
    path('running/', views.running),
    path('weight/', views.weight),
    path('QnA/', views.QnA),
    
]