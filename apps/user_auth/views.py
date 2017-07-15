from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .forms import LoginForm
from .forms import UserRegistrationForm
from .forms import ProfileRegistrationForm
from .forms import UserEditForm
from .forms import ProfileEditForm
from .models import Profile
from .models import Contact


def user_login(request):
    # Redirect the user to the dashboard if already signed in
    if request.user.is_authenticated:
        return redirect('dashboard')

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
    return render(request, 'account/login.html', {'form': form})


def register(request):
    # Redirect the user to the dashboard if already signed in
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileRegistrationForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile()
            profile_cleaned = profile_form.cleaned_data
            setattr(profile, 'user', new_user)
            setattr(profile, 'gender', profile_cleaned['gender'])
            setattr(profile, 'date_of_birth', profile_cleaned['date_of_birth'])
            profile.save()

            user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse('Disabled account')

            #return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        profile_form =  ProfileRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form})
