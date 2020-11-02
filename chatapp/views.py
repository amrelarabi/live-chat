from django.shortcuts import render

# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'chatapp/index.html', {})


def room(request, room_name):
    return render(request, 'chatapp/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

