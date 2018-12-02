from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from player.models import Player, Team, TeamMember
from api.serializers import PlayerSerializer
from player.handlers.TeamHandler import TeamHandler


class PlayerInfoView(APIView):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    #serializer_class = PlayerSerializer

    def get(self, request,  *args, **kwargs):
        user = request.user

        return Response(
            {
                'player_name': user.first_name,
                'player_age': user.player.age,
                'player_sex': user.player.sex.upper()
            },
            status=status.HTTP_200_OK
        )

class PlayerTeamListView(APIView):
    """
    Returns a list of all the teams the user is part of.
    List includes: Team Name, Team Rating and Player's Jersey Number
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    def get(self, request,  *args, **kwargs):

        user = request.user
        team_handler = TeamHandler()

        team_list = team_handler.get_teams_list(user=user)

        return Response(
            {
                'team_list': team_list
            },
            status=status.HTTP_200_OK
        )
