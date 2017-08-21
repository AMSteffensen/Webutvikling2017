from django.shortcuts import render


def messages(request):
    return render(request, 'messages/messages.html')
