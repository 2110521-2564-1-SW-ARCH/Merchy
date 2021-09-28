from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.render_inventory, name='entries'),
    path('<str:entry_id>', views.render_entry, name='entry'),
    path('update', views.update_entry, name='update'),
    path('delete', views.delete_entry, name='delete')
]
