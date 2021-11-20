from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('item', views.item_list),
    path('item/<str:id>', views.item_detail),
]