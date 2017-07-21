from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Team
from .models import TeamUser
from .models import TeamJoin
from .forms import TeamCreateForm
from notification.models import Notification
from snippets.unique_slug import unique_slugify


def team_list(request):
    # Get all public teams
    teams = Team.get.public()
    # Get all teams you're waiting to join
    pending = TeamJoin.get.pending(request.user)
    # Get all teams you are a member of
    memberOf = TeamUser.get.memberOf(request.user)
    return render(request, 'team/list.html', {'teams': teams, 'memberOf': memberOf, 'pending': pending})


def team_detail(request, slug):
    if request.method == 'POST':
        team_pk = request.POST.get('delete_team', '')
        try:
            teamObj = get_object_or_404(Team, pk=team_pk)
        except Http404:
            return redirect('team:team_list')

        team_name = teamObj.name
        teamObj.delete()
        return render(request, 'team/team_deleted.html', {'team_name': team_name})

    else:
        # trying to get a published project
        try:
            teamObj = get_object_or_404(Team, slug=slug, status='public')
        # it failed, try to get a hidden project for your user
        except Http404:
            try:
                teamObj = get_object_or_404(Team, slug=slug, status='private')
            # it failed, return 404
            except Http404:
                return redirect('team:team_list')

        # Get members of this team
        members = TeamUser.get.members(teamObj)

        return render(request, 'team/detail.html', {'team': teamObj, 'members': members})


@login_required
def team_create(request):
    if request.method == 'POST':
        team_form = TeamCreateForm(data=request.POST)
        if team_form.is_valid():
            team_item = team_form.save(commit=False)
            team_item.author = request.user
            if not team_item.slug:
                slug_str = "{}".format(team_item.name)
                unique_slugify(team_item, slug_str)
            team_item.save()

            memberOfTeam = TeamUser(team_id=team_item, user_id=request.user)
            memberOfTeam.save()

            return redirect(team_item.get_absolute_url())
    else:
        team_form = TeamCreateForm()
    return render(request, 'team/create.html', {'team_form': team_form})


@login_required
def team_mine(request):
    memberOf = TeamUser.objects.filter(user_id=request.user)
    teams = [getattr(team, 'team_id') for team in memberOf]
    return render(request, 'team/my_teams.html', {'teams': teams})


@ajax_required
@require_POST
@login_required
def team_req_join(request):
    teamPK = request.POST.get('team')
    action = request.POST.get('action')
    print("ajax submit")

    try:
        team = get_object_or_404(Team, pk=teamPK)
    except Http404:
        print("team not found", teamPK)
        return JsonResponse({'status': 'ko'})

    author = team.author

    if TeamJoin.objects.filter(user_ask=request.user,
                               team_id=team,
                               invited=False,
                               accepted=False).exists():
        print("Did exist")
        return JsonResponse({'status': 'ko'})

    print("Did not exist")
    notif_req = Notification(
        user_from=request.user,
        user_to=author,
        foreignPK=teamPK,
        context='team',
        action=action,
    )
    notif_req.save()

    team_req = TeamJoin(
        user_ask=request.user,
        team_id=team,
        invited=False,
        accepted=False
    )
    team_req.save()

    print("Created!")
    return JsonResponse({'status': 'ok', 'team': teamPK})