import json

from channels.generic.websocket import AsyncWebsocketConsumer

from account.models import User
from .models import UserCoordinate

class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_id = "navigation_%s" % self.room_id

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

        print("SOCKET MESSAGE: \n {} \n".format(text_data_json))

        user_id = text_data_json["user_id"]
        coord_x = text_data_json["coordinate_x"]
        coord_y = text_data_json["coordinate_y"]

        await self.channel_layer.group_send(
            self.room_group_id, 
            {
                "type": "info",
                "user_id": user_id,
                "coordinate_x": coord_x,
                "coordinate_y": coord_y,
            }
        )

    async def info(self, event):
        user_id = event["user_id"]
        coordinate_x = event["coordinate_x"]
        coordinate_y = event["coordinate_y"]

        await self.send(
            text_data=json.dumps({
                "user_id": user_id,
                "coordinate_x": coordinate_x,
                "coordniate_y": coordinate_y,
            })
        )
