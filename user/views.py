from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm, LoginForm

# Create your views here.
def test(request):
    username = 'test'
    password = 'test1234!!'
    #user = authenticate(username=username, password=password)
    messages.error(request, 'Error wrong username/password')
    user = User.objects.get(pk=1)
    #login(request, user)

    context = {
        "user": user,
        "password": password
    }

    return render(request, 'user/test.html', context)

@login_required
def profile(request):
    user = request.user
    profile = request.user.profile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user.first_name = user_form.cleaned_data['first_name']
            user.save()
            profile.birtdhay = profile_form.cleaned_data['birthday']
            profile.save()

            return redirect('user:profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)

    context = {
        "profile": profile,
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, 'user/profile.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            try:
                validate_password(user_form.cleaned_data['password'])
            except:
                return redirect('user:register')
            password = user_form.cleaned_data['password']

            user = User(username=username, email=email)
            user.set_password(password)
            user.save()

            return redirect('user:login')
    else:
        user_form = UserForm()

    context = {
        "user_form": user_form,
    }

    return render(request, 'user/register.html', context)


def login_user(request):
    if request.method == 'POST':
        login_form  = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('user:profile')
            else:
                messages.error(request, 'Login failed!')
                return redirect('user:login')
    else:
        login_form = LoginForm()

    context = {
        "login_form": login_form
    }

    return render(request, 'user/login.html', context)


@login_required
def logout_user(request):
    logout(request)

    return redirect('user:login')
