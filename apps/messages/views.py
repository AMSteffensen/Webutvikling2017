from django.shortcuts import render
from django.shortcuts import redirect

from messages.models import MessageRelation

from snippets.hasher import decode_value


def messages(request):
    return render(request, 'messages/messages.html')


def new_message(request):
    if request.method != 'POST':
        return redirect(request.META.get('HTTP_REFERER'))

    # Get data
    userHash = request.POST.get('new-message', '')
    if not userHash:
        print("NO USER HASH")
        return redirect(request.META.get('HTTP_REFERER'))

    user_id = int(decode_value(userHash))

    # If message relation does not exist
    if (not MessageRelation.objects.filter(userA_id=user_id, userB=request.user).exists()
        and not MessageRelation.objects.filter(userA=request.user, userB_id=user_id).exists()):
        # Create message relation
        relation = MessageRelation(userA=request.user, userB_id=user_id)
        relation.save()

    return redirect('msg:messages')
