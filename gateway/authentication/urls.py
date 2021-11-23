from django.conf.urls import url
from django.urls import path
from authentication import views 
 
urlpatterns = [ 
    path('user', views.user_list),
    # path('user/<str:pk>', views.user_detail),
    path('login', views.login),
    path('logout', views.logout),
    path('lazada/login', views.get_lazada_login_link),
    path('lazada/access-token', views.get_lazada_access_token),
    path('lazada/seller-id', views.get_lazada_seller_id),
]
