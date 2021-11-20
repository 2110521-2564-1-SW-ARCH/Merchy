from django.urls import path
from . import views

urlpatterns = [
    path('trackbybarcodes', views.shipping_status_list),
    path('order', views.order_list),
    path('order/<str:id>', views.order_detail),
]