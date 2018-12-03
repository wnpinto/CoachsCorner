from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from player.models import Player, Team, TeamMember
from api.serializers import PlayerSerializer
from player.handlers.TeamHandler import TeamHandler
from player.validators.TeamValidator import TeamValidator


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

class AddNewTeamView(APIView):
    """
    Creates a new team instance for the user and the sport provided.
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    def post(self, request, format=None):

        user = request.user
        data = request.data
        team_name = data.get('team_name', None)
        slogan = data.get('slogan', None)
        sport = data.get('sport', None)
        jersey_num = data.get('jersey_num', None)


        team_validator = TeamValidator()

        if team_validator.validate_team(team_name=team_name, slogan=slogan, sport=sport, user_jersey_num=jersey_num):
            team_handler = TeamHandler()
            sp = team_handler.get_or_create_sport(sport)
            team_handler.create_new_team(user=user, team_name=team_name, slogan=slogan, sport=sp, user_jersey_num=jersey_num)
            return Response(
            {},
            status=status.HTTP_200_OK
            )
        else:
            return Response(
        {
            'result': 'Validation failed for creating a new team'
        },
        status=status.HTTP_400_BAD_REQUEST
    )

class TeamListView(APIView):
    """
    Returns a list of all the teams.
    List includes: Team Name, Team Sport and Team Rating
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    def get(self, request,  *args, **kwargs):
        team_handler = TeamHandler()

        team_list = team_handler.get_team_list()

        return Response(
            {
                'team_list': team_list
            },
            status=status.HTTP_200_OK
        )

class TeamMembersListView(APIView):
    """
    Returns a list of all the teams.
    List includes: Team Name, Team Sport and Team Rating
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    def get(self, request,  *args, **kwargs):
        team_handler = TeamHandler()

        team_memebrs_list = team_handler.get_team_members(team=kwargs.get('pk', None))

        return Response(
            {
                'team_memebrs_list': team_memebrs_list
            },
            status=status.HTTP_200_OK
        )

class AddNewTeamMemberView(APIView):
    """
    Adds a new team member to the specified team id.

    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    def post(self, request, format=None):

        user = request.user
        data = request.data
        team_name = data.get('team_name', None)
        sport = data.get('sport', None)
        jersey_num = data.get('jersey_num', None)


        team_validator = TeamValidator()

        if team_validator.validate_new_team_member(user=user, team_name=team_name, sport=sport, user_jersey_num=jersey_num):
            team_handler = TeamHandler()
            team_handler.add_new_team_member(user=user, team_name=team_name, sport=sport, user_jersey_num=jersey_num)
            return Response(
            {},
            status=status.HTTP_200_OK
            )
        else:
            return Response(
        {
            'result': 'Validation failed for adding a new team member'
        },
        status=status.HTTP_400_BAD_REQUEST
    )