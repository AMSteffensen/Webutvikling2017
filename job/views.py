from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .forms import PostCreateForm
from .models import Post



def post_list(request):
    posts = Post.published.all()
    return render(request, 'job/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    if request.method == 'POST':
        post_pk = request.POST.get('delete_post', '')

        try:
            post = get_object_or_404(Post, pk=post_pk)
        except Http404:
            return redirect('job:post_list')

        post_title = post.title
        post.delete()
        return render(request, 'job/post/post_deleted.html', {'post_title': post_title})

    else:
        # Trying to get a published post
        try:
            post = get_object_or_404(Post, slug=post, status='publisert', publish__year=year, publish__month=month, publish__day=day)
        # It failed, try to get a drafted post for your user
        except Http404:
            try:
                post = get_object_or_404(Post, slug=post, status='mal', author=request.user, publish__year=year, publish__month=month, publish__day=day)
            # It failed, return 404
            except Http404:
                return redirect('job:post_list')
        return render(request, 'job/post/detail.html', {'post': post})


@login_required
def post_mine(request):
    #objects.filter(is_active=True).extra(select={'lower_first_name': 'lower(first_name)'}).order_by('lower_first_name')
    posts = Post.objects.filter(author=request.user)
    return render(request, 'job/post/myposts.html', {'posts': posts})


@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostCreateForm(data=request.POST)
        if post_form.is_valid():
            post_item = post_form.save(commit=False)
            post_item.author = request.user
            if not post_item.slug:
                post_item.slug = slugify(post_item.title)
            post_item.save()
            messages.success(request, 'Profile update successfully')
            return redirect(post_item.get_absolute_url())
        else:
            messages.error(request, 'Error updating your profile')
    else:
        post_form = PostCreateForm()
    return render(request, 'job/post/create.html', {'post_form': post_form})
