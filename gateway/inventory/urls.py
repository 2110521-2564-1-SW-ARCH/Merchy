from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('order', views.order_list),
    path('order/<str:id>', views.order_detail),
    path('item', views.item_list),
    path('item/<str:id>', views.item_detail),
]