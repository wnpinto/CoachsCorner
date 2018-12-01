from django.urls import include, path

from .views import authenticate_player
from .views.views import PlayerInfoView, PlayerTeamsOverviewView
from .views.home_view import HomeView
from .views.form_views import createnewteam

urlpatterns = [
    path('login/', authenticate_player.LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('home/playerinfo/', PlayerInfoView.as_view(), name='playerinfo'),
    path('home/playerteams/', PlayerTeamsOverviewView.as_view(), name='player_teams'),
    path('home/createnewteam', createnewteam, name='create_new_team')
]