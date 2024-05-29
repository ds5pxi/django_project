from django.urls import path, re_path
from . import views

urlpatterns= [
<<<<<<< HEAD
    path('', views.info),
    path('info/', views.info),
    path('running/', views.running),
    path('weight/', views.weight),
    path('QnA/', views.QnA),
    path('runningtip/', views.runningtip),
    path('weighttip/', views.weighttip),
    path('add/', views.add),
=======
    path('', views.index),
    path('/', views.index),
    path('views/', views.views),
    path('views/edit/', views.edit),
    path('write/', views.write),
>>>>>>> d6bbcdf8ac7d6c88a329a6c773426b1e2f05cc22
]