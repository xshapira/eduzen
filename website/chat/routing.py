from django.conf.urls import url

from . import consumers

websocket_urlpatterns = (
    url(r"^chat/telegram/$", consumers.TelegramBotConsumer),
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
)
