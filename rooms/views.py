from django.shortcuts import render
from .models import Room

def room_list(request):
    rooms = Room.objects.all().order_by('room_number')
    context = {'rooms': rooms}
    return render(request, 'rooms/room_list.html', context)
