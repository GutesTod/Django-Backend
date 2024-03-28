from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('users/add/', views.AddUsers, name='add_users'),
    path('users/', views.GetUsers, name='get_users')
]