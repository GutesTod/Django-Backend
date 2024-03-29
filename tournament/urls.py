from django.urls import path
from . import views

urlpatterns = [
    #path('', ..., name='home'),
    #path('players/add/match/', ..., name='add_users_to_match'),
    #path('players/add/stage/', ..., name='get_users_to_stage'),
    path('matchs/get/', views.GetMatchs, name="get_matchs"),
    #path('get/', ..., name="get_tournaments"),
    path('register/', views.RegisterTournament, name="register_tournaments")
]
