from django.urls import path
from .import views

app_name = 'RB'

urlpatterns = [
    path('register/', views.createAccount, name = "R"),
]