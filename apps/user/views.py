from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from common.decorators import ajax_required

from .forms import UserEditForm
from .forms import ProfileEditForm
from .models import Contact
from .models import WorkHour

from project.models import Project
from notification.models import Notification

from snippets.hasher import decode_value

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(request.user.get_absolute_url())
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'user/settings/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def dashboard(request):
    return render(request, 'user/other/dashboard.html', {'section': 'dashboard'})


@login_required
def user_list(request):
    #users = User.objects.filter(is_active=True).order_by('first_name')
    users = User.objects.filter(is_active=True).extra(select={'lower_first_name': 'lower(first_name)'}).order_by('lower_first_name')
    return render(request, 'user/users/list.html', {'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'user/profile/profile.html', {'user': user})


@login_required
def user_settings(request):
    return render(request, 'user/settings/settings.html')


@login_required
def user_relations(request):
    isFollowing = Contact.get.isFollowing(request.user)
    followers = Contact.get.followers(request.user)
    return render(request, 'user/other/relations.html', {'isFollowing': isFollowing,
                                                           'followers': followers})


@ajax_required
@require_POST
@login_required
@csrf_exempt
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
            print("jamann")
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})


@login_required
def user_stats(request):

    hour_entries = WorkHour.get.user_entries(request.user)

    return render(request, 'user/stats/stats.html', {'logged': hour_entries})



@login_required
def user_stats_add_hours(request):
    if request.method == 'POST':
        keys = ['date', 'project', 'sProject', 'hours', 'minutes' 'note']
        entries = []

        for ent in range(1, int((len(request.POST) - 1) / len(keys))):
            char = str(ent)

            # Check if this entry is entered
            if int(request.POST['hours' + char]) != 0 or int(request.POST['minutes' + char]) != 0:
                entry = {}
                entry['date'] = request.POST['date' + char]
                entry['project'] = decode_value(request.POST['project' + char])
                entry['sProject'] = request.POST['sProject' + char]
                entry['hours'] = request.POST['hours' + char]
                entry['minutes'] = request.POST['minutes' + char]
                entry['note'] = request.POST['note' + char]
                entries.append(entry)

                work = WorkHour(user=request.user,
                                work_date=entry['date'],
                                work_project_id=entry['project'],
                                work_category=entry['sProject'],
                                work_duration=entry['hours'] + ":" + entry['minutes'],
                                work_note=entry['note']
                                )
                work.save()


    projects = Project.objects.all().order_by('title')
    categories = [i[0] for i in WorkHour.CATEGORY_CHOICES]
    return render(request, 'user/stats/add_hours.html', {'categories': categories, 'projects': projects})


@login_required
def user_feed(request):
    unread_notif = Notification.get.unread(request.user)
    read_notif = Notification.get.read(request.user)
    return render(request, 'user/feed/feed.html', {'ur_notif': unread_notif, 'r_notif': read_notif})


