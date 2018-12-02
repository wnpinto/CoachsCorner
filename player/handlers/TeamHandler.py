from ..models import Team, TeamMember, Sport, User


class TeamHandler:
    """
    Handler class that processes any Team related logid
    """

    def create_new_team(self, user, team_name, slogan, sport, user_jersey_num):
        player = user.player

        team_obj = Team()
        team_obj.name = team_name
        team_obj.sport_id = sport.id
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
