from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_start, name ='home'),
]