from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

from team.models import TeamUser
from .models import Notification

from snippets.hasher import decode_data


@ajax_required
@require_POST
@login_required
def team_handel_req(request):
    # Get POST data
    payload = request.POST.get('payload')
    action = request.POST.get('action')
    context = request.POST.get('context')

    print(context)
    return JsonResponse({'status': 'ko'})

    # Verify the payload
    try:
        data = decode_data(payload)
    except Exception:
        return JsonResponse({'status': 'ko'})

    # Extract data
    user_id = int(data[0])
    team_id = int(data[1])

    # Verify the person is still waiting
    try:
        notif_req = Notification.objects.get(
            user_from=user_id,
            user_to=request.user,
            foreignPK=team_id,
            context=Notification.contexts.team.name,
            action=Notification.actions.team_req_join.name,
            url=payload,
            read=False,
        )
    except Exception:
        return JsonResponse({'status': 'ko'})

    # Mark the notification as read
    notif_req.read = True
    notif_req.save()

    # Create a notification for the requester
    if action == 'accept':
        new_action = Notification.actions.team_req_acc.name

        # Add user as member of team
        newMember = TeamUser(team_id_id=team_id, user_id_id=user_id)
        newMember.save()
    else:
        new_action = Notification.actions.team_req_dec.name

    notif_ans = Notification(
        user_from=request.user,
        user_to_id=user_id,
        foreignPK=team_id,
        context=Notification.contexts.team.name,
        action=new_action,
        read=False,
    )
    notif_ans.save()

    return JsonResponse({'status': 'ok'})