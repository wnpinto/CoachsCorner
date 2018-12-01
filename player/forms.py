from django import forms


class CreateTeamForm(forms.Form):

    team_name = forms.CharField(label='Team Name', max_length=100)
    team_sport = forms.CharField(label='Sport', max_length=100)
    slogan = forms.CharField(label='Slogan', max_length=30, required=False)
    player_number = forms.IntegerField(label='Player Number')
