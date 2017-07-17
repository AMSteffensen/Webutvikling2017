from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Team


def team_list(request):
    teams = Team.everything.all()
    return render(request, 'team/list.html', {'teams': teams})


def team_detail(request, slug):
    # trying to get a published project
    try:
        teamObj = get_object_or_404(Team, slug=slug, status='shown')
    # it failed, try to get a hidden project for your user
    except Http404:
        print("error 1", slug)
        try:
            teamObj = get_object_or_404(Team, slug=slug, status='hidden')
        # it failed, return 404
        except Http404:
            print("error 2")
            return redirect('team:team_list')
    return render(request, 'team/detail.html', {'team': teamObj})