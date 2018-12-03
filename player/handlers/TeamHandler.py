from ..models import Team, TeamMember, Sport, User


class TeamHandler:

    """
    Handler class that processes any Team related logid
    """

    def create_new_team(self, user, team_name, slogan, sport, user_jersey_num):
        """
        Creates a new team instance for the user and the sport provided.

        :param user:
        :param team_name:
        :param slogan:
        :param sport:
        :param user_jersey_num:
        :return:
        """
        player = user.player

        team_obj = Team()
        team_obj.name = team_name
        team_obj.sport_id = sport
        team_obj.slogan = slogan
        team_obj.save()

        team_member_obj = TeamMember()
        team_member_obj.player_id = player
        team_member_obj.team_id = team_obj
        team_member_obj.player_number = user_jersey_num
        team_member_obj.save()

        return team_obj

    def get_or_create_sport(self, sport):
        """
        creates a sport for the team. If a sport has already been created,
        just use that. Otherwise create a new sport.

        :param sport:
        :return:
        """

        existing_sport = Sport.objects.filter(name=sport)

        if not existing_sport:
            sport_obj = Sport()
            sport_obj.name = sport
            sport_obj.save()
            return sport_obj

        return existing_sport[0]

    def get_teams_list(self, user):
        """
        Returns a list of all the teams a user is part of

        :param user:
        :return:
        """
        player = user.player

        team_member_list = TeamMember.objects.filter(player_id=player.id)

        team_list = []

        for team_member in team_member_list:
            team = team_member.team_id

            team_list.append(
                {
                    'team_name': team.name,
                    'team_rating': team.rating,
                    'team_member_player_number': team_member.player_number
                }
            )

        return team_list

    def get_team_list(self):
        """
        Returns a list of all the teams

        :param user:
        :return:
        """

        team_list = Team.objects.all()

        list = []

        for team in team_list:

            list.append(
                {
                    'team_name': team.name,
                    'team_rating': team.rating,
                    'sport': team.sport_id.name
                }
            )

        return list

    def add_new_team_member(self, user, team_name, sport, user_jersey_num):
        """
        adds a player to a team. Must specify the sport since one team can have multiple sports.

        :param user:
        :param team_name:
        :param sport:
        :return:
        """

        team = Team.objects.filter(name=team_name, sport_id__name=sport)
        new_team_member = TeamMember()
        new_team_member.team_id = team[0]
        new_team_member.player_id = user.player
        new_team_member.player_number = user_jersey_num
        new_team_member.save()

        return new_team_member
