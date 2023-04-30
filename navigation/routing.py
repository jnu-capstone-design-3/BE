from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    re_path(r"navi/(?P<room_name>\w+)/$", consumers.Consumer.as_asgi()),
]