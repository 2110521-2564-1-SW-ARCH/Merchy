from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('entry', views.entry_list),
    path('entry/<str:id>', views.entry_detail),
    path('item', views.item_list),
    path('item/<str:id>', views.item_detail),
]