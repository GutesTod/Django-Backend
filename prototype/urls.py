from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('users/add/', views.AddUsers, name='add_users'),
    path('users/', views.GetUsers, name='get_users'),
    path('users/del/', views.DelUser, name = 'del_user'),
    path('user/', views.FindUser, name="find_user")
]