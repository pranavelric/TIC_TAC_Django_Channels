from  django.urls import path, include
from .views import *


urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('play/<room_code>',Play.as_view(),name="play")
]