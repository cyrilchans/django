
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('index/', views.index),
]
