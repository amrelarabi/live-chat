from django.shortcuts import render

# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

import chatapp
from chatapp.forms import SignUpForm
from chatapp.models import User


def index(request):
    return render(request, 'chatapp/index.html', {})


def room(request, room_name):
    return render(request, 'chatapp/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def signup(request):
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

            user = User.objects.create_user( email,
                                            password)
            user.save()
            if user:
                print("TEST")
        context = {'form': form}
        return render(request, 'chatapp/signup.html', context=context)
