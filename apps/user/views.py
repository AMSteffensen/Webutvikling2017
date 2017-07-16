from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .forms import UserEditForm
from .forms import ProfileEditForm
from .models import Contact



@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'user/profile/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def dashboard(request):
    return render(request, 'user/profile/dashboard.html', {'section': 'dashboard'})


@login_required
def user_list(request):
    #users = User.objects.filter(is_active=True).order_by('first_name')
    users = User.objects.filter(is_active=True).extra(select={'lower_first_name': 'lower(first_name)'}).order_by('lower_first_name')
    return render(request, 'user/users/list.html', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'user/users/detail.html', {'section': 'people', 'user': user})


@login_required
def user_settings(request):
    return render(request, 'user/profile/settings.html')


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})
