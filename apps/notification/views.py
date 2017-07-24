from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

from team.models import TeamJoin
from team.models import TeamUser
from .models import Notification

from snippets.hasher import decode_data


@ajax_required
@require_POST
@login_required
def team_handel_req(request):

    payload = request.POST.get('payload')
    action = request.POST.get('action')

    # Verify the payload
    try:
        data = decode_data(payload)
    except Exception:
        return JsonResponse({'status': 'ko'})

    user_id = int(data[0])
    team_id = int(data[1])

    # Verify the person is still waiting
    joinObj = TeamJoin.objects.filter(user_ask=user_id, team_id=team_id, invited=False)
    if not joinObj:
        return JsonResponse({'status': 'ko'})

    # Mark the notification as read
    notif_req = Notification.objects.get(
        user_from=user_id,
        user_to=request.user,
        foreignPK=team_id,
        context='team',
        action='team_req_join',
        url=payload,
        read=False,
    )
    notif_req.read = True
    notif_req.save()

    if action == 'accept':
        # Add user as member of team
        newMember = TeamUser(team_id_id=team_id, user_id_id=user_id)
        newMember.save()

    # Delete TeamJoin object
    joinObj.delete()

    return JsonResponse({'status': 'ok'})