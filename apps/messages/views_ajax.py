from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

from .models import MessageRelation
from .models import Message

from snippets.hasher import decode_value


@ajax_required
@require_POST
@login_required
def send_pm(request):
    # Get POST data
    msg = request.POST.get('msg')
    value = request.POST.get('rel')

    print("value:", value)
    print("msg:", msg)


    # Verify the hash
    try:
        data = decode_value(value)
    except Exception:
        print("Bad hash")
        return JsonResponse({'status': 'ko'})

    # Extract data
    msg_rel_id = int(data[0])

    # Get other user
    try:
        msgRelObj = MessageRelation.objects.get(pk=msg_rel_id)
    except Exception:
        print("Invalid PK")
        return JsonResponse({'status': 'ko'})

    if msgRelObj.userA == request.user:
        otherUser = msgRelObj.userB
    else:
        otherUser = msgRelObj.userA

    # Create a new message
    new_msg = Message(msg_id=msgRelObj,
                      user_from=request.user,
                      user_to=otherUser,
                      message=msg)
    new_msg.save()

    return JsonResponse({'status': 'ok', 'msg':new_msg.pk,'user':request.user.pk,'rel':value})
