from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.all_users, name='users'),  # ourdomain.com/gateway/users
    path('users/<int:user_id>', views.user_details, name='user'),  # ourdomain.com/gateway/users/1
    path('add_user', views.add_user, name='add_user'), # ourdomain.com/gateway/add_user
    path('update_user/<int:user_id>', views.update_user, name='update_user'), # ourdomain.com/gateway/update_user/1
    path('del/<int:user_id>', views.del_user, name='del_user'),
    path('', views.landing_page),
]
