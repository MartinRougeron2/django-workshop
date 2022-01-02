from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import SignUpForm, LoginForm
from users.models import BirddyTor


def signup(request):
    print(request.user)
    if request.user.is_authenticated or not request.user.is_anonymous:
        return redirect('index')
    if request.method == "POST":  # submit
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']

            if password == password_confirm:

                if len(User.objects.filter(username=username)) != 0:
                    form.add_error("username", "user already exists")
                else:
                    user = User.objects.create_user(username, password=password)
                    user.save()
                    birdydtor = BirddyTor(user=user, lang='fr')
                    birdydtor.save()
                    user = authenticate(request, username=username, password=password)
                    django_login(request, user)
                    return redirect('index')
            else:
                form.add_error("password_confirm", "passwords don't match")
    else:
        form = SignUpForm()
    return render(request, "signup.html", context={'form': form})


def login(request):
    print(request.user)
    if request.user.is_authenticated or not request.user.is_anonymous:
        return redirect('index')
    print(request.user)
    if request.method == "POST":  # submit
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if len(User.objects.filter(username=username)) == 0:
                form.add_error("username", "user doesn't exists")
                return render(request, "login.html", context={'form': form})
            if user is None:
                form.add_error("password", "bad password")
                return render(request, "login.html", context={'form': form})
            django_login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, "login.html", context={'form': form})


def logout(request):
    if not request.user.is_authenticated:
        return redirect('index')
    logout(request)
    return redirect('index')
