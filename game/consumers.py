import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Message
from random import randint

player_list = {}


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_group_name = 'chat_main'

    def new_message(self, data):
        author_user = player_list[self.channel_name]
        message = Message.objects.create(
            author=author_user,
            content=data['message'])
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def message_to_json(self, message):
        return {
            'author': message.author,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    def add_user(self, data):
        print("Otrzymano usera")
        player_list[self.channel_name] = data['username']
        print(player_list)
        self.send_new_user(data['username'])

    commands = {
        "new_message":  new_message,
        "add_user": add_user
    }

    def connect(self):
        # Join room group
        player_list[self.channel_name] = "Błąd"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

        del player_list[self.channel_name]

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        print(f"Otrzymano socket typu: {data['command']}")
        self.commands[data['command']](self, data)

        # Send message to room group
    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_new_user(self, user):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'user',
                'username': {"username": user}
            }
        )
    # Receive message from room group
    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def user(self, event):
        self.send(text_data=json.dumps(event['username']))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
