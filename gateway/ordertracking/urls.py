from django.contrib import admin
from django.urls import path
from ordertracking import views

urlpatterns = [
    path('', views.get_ordertracking_detail)
]