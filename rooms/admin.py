from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomADmin(admin.ModelAdmin):
    list_display = ('room_number', 'name', 'room_type', 'price_per_night', 'capacity', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('room_number', 'name')
