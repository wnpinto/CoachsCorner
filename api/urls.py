from django.conf.urls import url, include
from rest_framework import routers
from api import views
from .views import PlayerInfoView, PlayerTeamListView, AddNewTeamView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^getPlayerInfo/', PlayerInfoView.as_view(), name='player_info'),
    url(r'^getPlayerTeamList/', PlayerTeamListView.as_view(), name='player_team_list'),
    url(r'^addNewTeam/', AddNewTeamView.as_view(), name='add_new_team')
]