from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm, LoginForm, RegisterForm

@login_required
def profile(request):
    user = request.user
    profile = request.user.profile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user.save()
            profile.save()

            return redirect('user:profile')
        else:
            print('Fuuuck!')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "profile": profile,
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, 'user/profile.html', context)


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            validate_password(register_form.cleaned_data['password'])
            password = register_form.cleaned_data['password']

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()

            return redirect('user:login')
    else:
        register_form = RegisterForm()

    context = {
        "register_form": register_form,
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
