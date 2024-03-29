from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Team
from .models import TeamUser
from .forms import TeamCreateForm
from notification.models import Notification
from snippets.unique_slug import unique_slugify
from snippets.hasher import decode_value

def team_list(request):
    # Get all public teams
    teams = Team.get.public()
    # Get all teams you're waiting to join
    pending_req = Notification.get.pending_team_req(request.user)
    # Get all teams you've been invited to
    pending_inv = Notification.get.pending_team_inv_by_user(request.user)
    # Get all teams you are a member of
    memberOf = TeamUser.get.memberOf(request.user)
    return render(request, 'team/list.html', {'teams': teams,
                                              'memberOf': memberOf,
                                              'pending_req': pending_req,
                                              'pending_inv': pending_inv,})


def team_detail(request, slug):
    if request.method == 'POST':
        team_hash = request.POST.get('delete_team', '')
        # Try to get the team pk
        try:
            team_pk = decode_value(team_hash)
        except Exception:
            return redirect('team:team_list')

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
        # Get all members
        all_users = User.objects.all()
        # Get pending invites
        pending_inv = Notification.get.pending_team_inv(teamObj.pk)
        pending_req = Notification.get.pending_team_req_by_team(teamObj.pk)

        return render(request, 'team/detail.html', {'team': teamObj,
                                                    'members': members,
                                                    'all_users': all_users,
                                                    'pending_inv': pending_inv,
                                                    'pending_req': pending_req})


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