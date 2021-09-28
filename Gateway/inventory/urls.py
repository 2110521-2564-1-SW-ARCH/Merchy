from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.render_inventory, name='entries'),
    path('create', views.create_entry, name='create'),
    path('update', views.update_entry, name='update'),
    path('delete', views.delete_entry, name='delete'),
    path('<str:entry_id>', views.render_entry, name='entry'),

    path('item', views.get_items, name='get_items'),
    path('item/create', views.create_item, name='create_item'),
    path('item/update', views.update_item, name='update_item'),
    path('item/delete', views.delete_item, name='delete_item'),
    path('item/<str:item_id>', views.get_item, name='get_item'),
]
