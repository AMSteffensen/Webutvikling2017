from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login

from user_auth.forms import LoginForm


def landing(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        return redirect('user:dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        ## Else; Errors are being called and showed in the html by django
    else:
        form = LoginForm()
    return render(request, 'front_page/landing.html', {'form': form})