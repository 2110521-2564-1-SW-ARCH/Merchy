from django.conf.urls import url
from django.urls import path
from authentication import views 
 
urlpatterns = [ 
    path('', views.user_list),
    path('login', views.login),
    path('logout', views.logout),
    path('<str:pk>', views.user_detail),
]
