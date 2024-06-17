from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import RoomForm
from .models import Talk, Room, CustomUser
from django.shortcuts import render
from .models import Room, Talk


def home(request):
    rooms = Room.objects.all()
    schedule = {}
    for room in rooms:
        schedule[room] = Talk.objects.filter(room=room)
    return render(request, 'conference/home.html', {'schedule': schedule})


@login_required
def talk_list(request):
    user = request.user
    if CustomUser.role == 'Speaker' or CustomUser.role == 'Admin' or user.is_superuser:
        talks = Talk.objects.all()
        room = Room.objects.all()
        users = CustomUser.objects.all()
        return render(request, 'conference/talk_list.html', {'talks': talks, 'room': room, 'users': users})
    else:
        return render(request, 'conference/access_denied.html')


@staff_member_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'conference/user_list.html', {'users': users})


@staff_member_required
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')  # Перенаправляем пользователя на главную страницу
    else:
        form = RoomForm()
    return render(request, 'conference/add_room.html', {'form': form})


def talk_detail(request, talk_id):
    talk = get_object_or_404(Talk, id=talk_id)
    return render(request, 'conference/talk_detail.html', {'talk': talk})
