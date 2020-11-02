from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

import chatapp
from chatapp.forms import *
from chatapp.models import *


@login_required
def index(request):
    return render(request, 'chatapp/index.html', {})


@login_required
def room(request, room_name):
    return render(request, 'chatapp/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def signup_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'chatapp/signup.html', context=context)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            if password != re_password:
                context = {'form': form, 'error_msg': 'Two passwords was not matched'}
                return render(request, 'chatapp/signup.html', context=context)
            if User.objects.filter(email=email).count() > 0:
                context = {'form': form, 'error_msg': 'This email is already exit'}
                return render(request, 'chatapp/signup.html', context=context)
            if User.objects.filter(username=username).count() > 0:
                context = {'form': form, 'error_msg': 'This username is already exit'}
                return render(request, 'chatapp/signup.html', context=context)
            user = User.objects.create_user(email, username, password)
            user.save()
            if user:
                user.first_name = f_name
                user.last_name = l_name
                return redirect('login')
            else:
                context = {'form': form, 'error_msg': 'Error While signup'}
                return render(request, 'chatapp/signup.html', context=context)
        context = {'form': form}
        return render(request, 'chatapp/signup.html', context=context)


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {'form': form}
        return render(request, 'chatapp/login.html', context=context)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                context = {'form': form,
                           'error_msg': 'Username or password is incorrect' }
                return render(request, 'chatapp/login.html', context=context)
        else:
            context = {'form': form,
                       'error_msg': 'Email or password is incorrect'}
            return render(request, 'chatapp/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('login')

