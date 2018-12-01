from django.shortcuts import render
from django.views.generic import TemplateView
from player.models import Team, Sport, TeamMember

from django.http import HttpResponse


class PlayerInfoView(TemplateView):
    template_name = 'fragment_player_info.html'

    def get_player(self, request):
        return request.user

    def get(self, request, *args, **kwargs):

        user = self.get_player(request)

        context = {
                   'player_name': user.first_name,
                   'player_age': user.player.age,
                   'player_sex': user.player.sex.upper()
                   }

        return render(request, self.template_name, context)


class PlayerTeamsOverviewView(TemplateView):
    template_name = 'fragment_player_teams_overview.html'

    def get_player(self, request):
        return request.user

    def get(self, request, *args, **kwargs):

        user = self.get_player(request)
        player_teams_list = TeamMember.objects.filter(player_id=user.player.id)

        context = {
                   'player_teams_list': player_teams_list,
                   }

        return render(request, self.template_name, context)
