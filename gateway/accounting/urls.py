from django.contrib import admin
from django.urls import path
from accounting import views

urlpatterns = [
    path('', views.getSales),
]