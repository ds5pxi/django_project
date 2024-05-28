from django.urls import path, re_path
from . import views

urlpatterns= [
    path('', views.info),
    path('info/', views.info),
    path('running/', views.running),
    path('weight/', views.weight),
    path('QnA/', views.QnA),
    
]