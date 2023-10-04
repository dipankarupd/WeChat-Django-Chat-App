from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.


def home(req):
    return render(req, 'home.html')


def rooms(req, rooms):
    username = req.GET.get('username')
    roomdetail = Room.objects.get(room=rooms)
    return render(req, 'rooms.html', {
        'username': username,
        'room': roomdetail
    })


def check(req):
    roomname = req.POST['room']
    username = req.POST['username']

    if Room.objects.filter(room=roomname).exists():
        return redirect('/'+roomname+'/?username='+username)

    else:
        new_room = Room.objects.create(room=roomname)
        new_room.save()
        return redirect('/'+roomname+'/?username='+username)