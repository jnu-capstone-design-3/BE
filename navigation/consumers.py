import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.permissions import IsAuthenticated


class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "navigation_%s" % self.room_name

        print(self.channel_name)
        print(self.room_group_name)
        print(self.room_name)

        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
            )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
            )

    async def receive(self, text_data):
        
        text_data_json = json.loads(text_data)

        message = text_data_json["message"]
        print('from rec', self.room_group_name)

        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                "type": "info",
                "message": message,
            }
        )

    async def info(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))