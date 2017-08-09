from django.shortcuts import render


def about(request):
    return render(request, 'support/about.html')

def contact(request):
    return render(request, 'support/contact.html')