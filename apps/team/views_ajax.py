from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Team
from notification.models import Notification
from snippets.hasher import encode_data
from snippets.hasher import decode_value


@ajax_required
@require_POST
@login_required
def team_req_join(request):
    # Get POST data
    teamHash = request.POST.get('team')
    # Try to decode the scrambled team pk
    try:
        teamPK = decode_value(teamHash)
    except Exception:
        print("bad hash")
        return JsonResponse({'status': 'ko'})

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


@ajax_required
@require_POST
@login_required
def team_invite(request):
    # Get POST data
    pass







