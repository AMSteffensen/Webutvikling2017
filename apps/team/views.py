from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Team
from .models import TeamUser
from .forms import TeamCreateForm
from notification.models import Notification
from snippets.unique_slug import unique_slugify
from snippets.hasher import encode_data

def team_list(request):
    # Get all public teams
    teams = Team.get.public()
    # Get all teams you're waiting to join
    pending = Notification.get.pending_team_req(request.user)
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
        all_users = User.objects.all()

        return render(request, 'team/detail.html', {'team': teamObj, 'members': members, 'all_users': all_users})


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
    # Get POST data
    teamPK = request.POST.get('team')

    # Try to get the team
    try:
        team = get_object_or_404(Team, pk=teamPK)
    except Http404:
        print("team not found", teamPK)
        return JsonResponse({'status': 'ko'})

    # Double check that the request does not already exist
    if Notification.objects.filter(
        user_from=request.user,
        user_to=team.author,
        foreignPK=teamPK,
        context=Notification.contexts.team.name,
        action=Notification.actions.team_req_join.name,
        read=False,
    ).exists():
        print("Did exist")
        return JsonResponse({'status': 'ko'})

    # Generate datahash
    print("Generating hash")
    notif_url = encode_data([request.user.pk, teamPK])
    print(notif_url)

    # Generate a request notification
    notif_req = Notification(
        user_from=request.user,
        user_to=team.author,
        foreignPK=teamPK,
        context=Notification.contexts.team.name,
        action=Notification.actions.team_req_join.name,
        url=notif_url,
    )
    notif_req.save()

    # Return a successful response
    return JsonResponse({'status': 'ok', 'team': teamPK})