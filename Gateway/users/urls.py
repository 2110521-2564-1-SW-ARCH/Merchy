from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users, name='users'),  # ourdomain.com/users
    path('<int:user_id>', views.user_details, name='user'),  # ourdomain.com/users/1
    path('add_user', views.add_user, name='add_user'), # ourdomain.com/users/add_user
    path('update_user/<int:user_id>', views.update_user, name='update_user'), # ourdomain.com/users/update_user/1
    path('del/<int:user_id>', views.del_user, name='del_user'),
    path('landing_page', views.landing_page, name='landing_page'),
]
