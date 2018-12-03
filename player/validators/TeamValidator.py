from player.models import Team, TeamMember

class TeamValidator:
    """
    Validator class that validates Team related data/logic
    """

    def validate_team(self, team_name, slogan, sport, user_jersey_num):
        if team_name and sport and user_jersey_num:
            existing_team = Team.objects.filter(name=team_name)

            if existing_team:
                return False
        else:
            return False

        return True

    def validate_new_team_member(self, user, team_name, sport, user_jersey_num):
        """
        validate that the player dosen't already exist for the team and it's sport.

        :param user:
        :param team_name:
        :param sport:
        :param user_jersey_num:
        :return:
        """
        if user and team_name and sport and user_jersey_num and not TeamMember.objects.filter(
                player_id=user.player,
                team_id__name=team_name,
                team_id__sport_id__name=sport):
            return True
        else:
            return False
