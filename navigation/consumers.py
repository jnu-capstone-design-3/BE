import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.permissions import IsAuthenticated


class Consumer(AsyncWebsocketConsumer):
    permisssions = [IsAuthenticated,]

    async def connect(self):
        
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_id = "navigation_%s" % self.room_id
        self.user = self.scope["user"]

        print(self.channel_name)
        print(self.room_group_id)
        print(self.room_id)

        await self.channel_layer.group_add(
            self.room_group_id, 
            self.channel_name
            )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_id, 
            self.channel_name
            )

    async def receive(self, text_data):
        
        text_data_json = json.loads(text_data)

        message = text_data_json["message"]
        print('from rec', self.room_group_id)

        await self.channel_layer.group_send(
            self.room_group_id, 
            {
                "type": "info",
                "message": message,
            }
        )

    async def info(self, event):
        message = event["message"]

        await self.send(
            text_data=json.dumps({
                    "message": message
                    }
                )
            )