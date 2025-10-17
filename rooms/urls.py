from django.urls import path
from . import views

app_name = 'rooms' # Namespace per l'app
urlpatterns = [
    path('', views.room_list, name='room_list'),
]