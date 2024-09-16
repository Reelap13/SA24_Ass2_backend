from typing import List

from .chat_saver import *
from .message import Message

class ChatManager():
    def __init__(self):
        self.messages: List[Message] = load_messages()


    async def add_message(
            self,
            message: Message
    ):
        self.messages.append(message)
        save_messages(self.messages)


    async def get_messages(self) -> dict:
        return [message.dict() for message in self.messages]


    async def get_messages_count(self) -> dict:
        return len(self.messages)

chat = ChatManager()
