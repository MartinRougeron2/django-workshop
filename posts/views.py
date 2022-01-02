from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CommentForm, BirddyForm
from .models import Birddy, Comment
from users.models import BirddyTor


def index(request):
    return all_posts(request)


def all_posts(request):
    posts = Birddy.objects.all()
    context = {
        'posts': posts,
        'user': request.user
    }
    return render(request, 'home.html', context=context)


def detail(request, post_id):
    post = Birddy.objects.get(id=post_id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.author = BirddyTor.objects.get(user=request.user)
            comment.post = post
            comment.save()
            form.clean()
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'detail.html', context=context)


def vote_up(request, post_id):
    post = Birddy.objects.get(id=post_id)
    tor = BirddyTor.objects.get(user=request.user)
    post.liked_by.add(tor)
    post.disliked_by.remove(tor)
    post.save()
    return redirect('detail', post_id=post_id)


def vote_down(request, post_id):
    post = Birddy.objects.get(id=post_id)
    tor = BirddyTor.objects.get(user=request.user)
    post.disliked_by.add(tor)
    post.liked_by.remove(tor)
    post.save()
    return redirect('detail', post_id=post_id)


def add_post(request):
    if not request.user.is_authenticated or request.user.is_anonymous:
        return redirect('signup')
    form = BirddyForm()
    if request.method == "POST":  # submit
        form = BirddyForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']

            post = Birddy(title=title, desc=desc, author=BirddyTor.objects.get(user=request.user))
            post.save()

        return redirect('index')
    return render(request, 'add_post.html', context={'form': form})
