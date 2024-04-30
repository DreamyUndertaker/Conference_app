from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import RoomForm
from .models import Talk, Room, CustomUser


def home(request):
    rooms = Room.objects.all()
    schedule = {}
    for room in rooms:
        schedule[room] = Talk.objects.filter(room=room)
    return render(request, 'home/home.html', {'schedule': schedule})


@login_required
def talk_list(request):
    user = request.user
    if user.role == 'Speaker':
        talks = user.talks.all()
        return render(request, 'home/talk_list.html', {'talks': talks})
    else:
        return render(request, 'home/access_denied.html')


@staff_member_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'home/user_list.html', {'users': users})


def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')  # Перенаправляем пользователя на главную страницу
    else:
        form = RoomForm()
    return render(request, 'home/add_room.html', {'form': form})
