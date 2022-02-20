from django.urls import path
from .consumers import GameRoom


websocket_urlpatterns = [
    path('ws/game/<room_code>',GameRoom.as_asgi())
]