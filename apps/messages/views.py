from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import render_to_string
from messages.models import MessageRelation
from messages.models import Message

from snippets.hasher import decode_value


class MessageWrapper():
    def __init__(self, relation, msgs):
        self.relation = relation
        if msgs:
            if len(msgs) > 20:
                self.msgs = msgs.reverse()[:20].reverse()
            else:
                self.msgs = msgs
            rev = msgs.reverse()[0]
            self.last_msg = rev.message
            self.last_from = rev.user_from
        else:
            self.last_msg = "Ingen meldinger.."
            self.user_from = None


def messages(request):

    relations = MessageRelation.get.connections(request.user)

    wrapper = []
    for rel in relations:
        wrapper.append(MessageWrapper(rel, rel.msg_id.all()))

    return render(request, 'messages/messages.html', {'wrapper': wrapper})



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
