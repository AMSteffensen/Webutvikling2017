from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect

from messages.models import MessageRelation

from snippets.hasher import decode_value


def messages(request):

    connections = MessageRelation.get.connections(request.user)

    return render(request, 'messages/messages.html', {'connections': connections})



def new_message(request):
    if request.method != 'POST':
        return redirect(request.META.get('HTTP_REFERER'))

    # Get data
    userHash = request.POST.get('new-message', '')
    if not userHash:
        print("NO USER HASH")
        return redirect(request.META.get('HTTP_REFERER'))

    # Get User object
    user_id = int(decode_value(userHash))
    try:
        user = User.objects.get(pk=user_id)
    except:
        print("WRONG USER PK")
        return redirect(request.META.get('HTTP_REFERER'))


    # If message relation does not exist
    if not MessageRelation.objects.filter(userA__in=(user, request.user), userB__in=(user, request.user)).exists():
        # Create message relation
        relation = MessageRelation(userA=request.user, userB_id=user_id)
        relation.save()



    return redirect('msg:messages')