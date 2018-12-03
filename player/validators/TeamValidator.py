from player.models import Team

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
