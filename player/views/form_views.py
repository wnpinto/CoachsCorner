from django.shortcuts import render, redirect

from player import settings

from ..forms import CreateTeamForm

from ..models import Sport, Team, TeamMember, Player



def createnewteam(request):
    """
    Creates a new team and automatically assigns the team a team member (i.e. user)
    :param request:
    :return:
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateTeamForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            team_name = form.cleaned_data.get('team_name')
            team_sport = form.cleaned_data.get('team_sport')
            slogan = form.cleaned_data.get('slogan')
            player_number = form.cleaned_data.get('player_number')
            sp = Sport.objects.filter(name=team_sport)

            player = request.user.player

            if not sp:
                sport_obj = Sport()
                sport_obj.name = team_sport
                sport_obj.save()
                sp = sport_obj
            else:
                sp = sp[0]

            team_obj = Team()
            team_obj.name = team_name
            team_obj.sport_id = sp
            team_obj.slogan = slogan
            team_obj.save()

            team_member_obj = TeamMember()
            team_member_obj.player_id = player
            team_member_obj.team_id = team_obj
            team_member_obj.player_number = player_number
            team_member_obj.save()

            return redirect(settings.LOGIN_REDIRECT_URL)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateTeamForm()

    return render(request, 'fragment_create_new_team_form.html', {'form': form})
