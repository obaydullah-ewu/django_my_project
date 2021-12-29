import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.context_processors import media

from App_Dashboard.forms import PostForm
from App_Dashboard.models import Post
from App_Login.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile

# Create your views here.


def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        print(list(request.POST.items()))
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password1']
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            registered = True
            data_dict = {
                'user_id': user.id,
                'type': request.POST['type'],
            }
            UserProfile.objects.create(**data_dict)
            return HttpResponseRedirect(reverse('App_Login:login'))

    return render(request, 'App_Login/sign_up.html', context={'title': 'Sign Up', 'form': form})


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Dashboard:home'))
    return render(request, 'App_Login/login.html', context={'title': 'Login', 'form': form})


@login_required
def edit_profile(request):

    if request.user.is_superuser:
        messages.error(request, 'You are a superuser')
        return HttpResponseRedirect(reverse('App_Login:profile'))

    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)

        if request.FILES and request.POST.get('profile_pic-clear'):
            pass
        else:
            if request.FILES:
                if request.user.user_profile.profile_pic:
                    if os.path.exists(request.user.user_profile.profile_pic.path):
                        os.remove(request.user.user_profile.profile_pic.path)

            if request.POST.get('profile_pic-clear'):
                if request.user.user_profile.profile_pic:
                    if os.path.exists(request.user.user_profile.profile_pic.path):
                        os.remove(request.user.user_profile.profile_pic.path)

        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            messages.success(request, 'Profile Updated')
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/edit-profile.html', context={'title': 'Edit Profile', 'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required
def profile(request):
    form = PostForm()
    diction = {
        'title': 'User List',
        'form': form
    }
    return render(request, 'App_Login/user.html', context=diction)

@login_required
def users(request):
    users = UserProfile.objects.filter(type=2)
    print(users)
    diction = {
        'title': 'User List',
        'users': users
    }
    return render(request, "App_Login/users.html", context=diction)