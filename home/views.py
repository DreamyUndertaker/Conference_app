from django.shortcuts import render
from .models import Room, Talk


def home(request):
    rooms = Room.objects.all()
    schedule = {}
    for room in rooms:
        schedule[room] = Talk.objects.filter(room=room)
    return render(request, 'conference/home.html', {'schedule': schedule})
