from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse  

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


def send(req):
    message = req.POST['message']
    room_id = req.POST['room_id']
    username = req.POST['username']

    msg = Message.objects.create(username = username, message = message, room = room_id)
    msg.save()
    return HttpResponse('Message sent successfully')