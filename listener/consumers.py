from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('all_data', self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard('all_data', self.channel_name)

    async def send_data(self, event):
        response_data = event['data']
        data = json.dumps(response_data)

        await self.send(data)