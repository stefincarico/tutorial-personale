# rooms/models.py
from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('SGL', 'Singola'),
        ('DBL', 'Doppia'),
        ('SUI', 'Suite'),
    ]

    room_number = models.CharField(max_length=10, unique=True, verbose_name="Numero Camera")
    name = models.CharField(max_length=50, verbose_name="Nome Camera")
    room_type = models.CharField(max_length=3, choices=ROOM_TYPES, verbose_name="Tipo Camera")
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prezzo per Notte")
    capacity = models.PositiveIntegerField(verbose_name="Capacità")
    is_available = models.BooleanField(default=True, verbose_name="Disponibile")

    def __str__(self):
        return f"{self.name} ({self.get_room_type_display()}) - N° {self.room_number}"

    class Meta:
        verbose_name = "Camera"
        verbose_name_plural = "Camere"
