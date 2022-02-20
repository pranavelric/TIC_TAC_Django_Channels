from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.layers import get_channel_layer

class GameRoom(WebsocketConsumer):
    channel_layer = get_channel_layer()

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' % self.room_name
        print(self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
     
    
    def receive(self, text_data):
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type' : 'run_game',
                'payload' : text_data,
            },
        )

    
    def disconnect(self, code):
        print("Disconnect")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    def run_game(self,event):
        data = event['payload']
        data = json.loads(data)
        self.send(text_data=json.dumps({
            'payload':data['data']
        }))