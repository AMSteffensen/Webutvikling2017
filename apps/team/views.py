from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Team
from .models import TeamUser
from .forms import TeamCreateForm
from snippets.unique_slug import unique_slugify


def team_list(request):
    teams = Team.everything.all()
    return render(request, 'team/list.html', {'teams': teams})


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
            teamObj = get_object_or_404(Team, slug=slug, status='shown')
        # it failed, try to get a hidden project for your user
        except Http404:
            try:
                teamObj = get_object_or_404(Team, slug=slug, status='hidden')
            # it failed, return 404
            except Http404:
                return redirect('team:team_list')

        # Get members of this team
        teamUserObj = TeamUser.objects.filter(team_id=teamObj)
        members = [getattr(member, 'user_id') for member in teamUserObj]

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