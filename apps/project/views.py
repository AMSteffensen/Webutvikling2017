from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .forms import ProjectCreateForm
from .models import Project
from snippets.hasher import decode_value


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project/list.html', {'projects': projects})


def project_detail(request, year, month, day, slug):
    if request.method == 'POST':
        project_hash = request.POST.get('delete_project', '')

        # Try to decode the project pk
        try:
            project_pk = decode_value(project_hash)
        except Exception:
            return redirect('proj:project_list')
        try:
            projectObj = get_object_or_404(Project, pk=project_pk)
        except Http404:
            return redirect('proj:project_list')

        # Check if you actually own this project
        if projectObj.author == request.user:
            project_title = projectObj.title
            projectObj.delete()
            return render(request, 'project/project_deleted.html', {'project_title': project_title})

    # Trying to get a published project
    else:
        # Trying to get a published project
        try:
            projectObj = get_object_or_404(Project, slug=slug, created__year=year, created__month=month, created__day=day)
        # It failed, Redirect the user
        except Http404:
            return redirect('proj:project_list')

        return render(request, 'project/detail.html', {'project': projectObj})


@login_required
def project_mine(request):
    projects = Project.objects.filter(author=request.user)
    return render(request, 'project/my_projects.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        project_form = ProjectCreateForm(data=request.POST)
        if project_form.is_valid():
            project_item = project_form.save(commit=False)
            project_item.author = request.user
            if not project_item.slug:
                project_item.slug = slugify(project_item.title)
            project_item.save()
            messages.success(request, 'Project created successfully')
            return redirect(project_item.get_absolute_url())
        else:
            messages.error(request, 'Error creating your project')
    else:
        project_form = ProjectCreateForm()
    return render(request, 'project/create.html', {'project_form': project_form})


@login_required
def project_edit(request, year, month, day, slug):
    try:
        projectObj = get_object_or_404(Project, slug=slug, author=request.user, created__year=year, created__month=month, created__day=day)
    except Http404:
        return redirect('user:dashboard')

    # Restrict unallowed users
    if projectObj.author != request.user:
        print("Not owner")
        return redirect('user:dashboard')

    if request.method == 'POST':
        project_form = ProjectCreateForm(instance=projectObj, data=request.POST)
        if project_form.is_valid():
            project_item = project_form.save(commit=False)
            project_item.slug = slugify(project_item.title)
            project_item.save()
            return redirect(project_item.get_absolute_url())
        else:
            project_form = ProjectCreateForm(instance=projectObj)
    else:
        project_form = ProjectCreateForm(instance=projectObj)

    return render(request, 'project/edit.html', {'project_form': project_form})



















