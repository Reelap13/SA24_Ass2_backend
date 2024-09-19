from typing import List
import json
import os

from .message import Message

path = (
    "C:\\Users\\mixai\\Education\\SoftwareArchitecture\\"
    "Assignment02\\SA24_Ass2_backend\\data\\chat"
)


def load_messages() -> List[Message]:
    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump([], f)

    with open(path, 'r') as f:
        if os.stat(path).st_size == 0:
            return []
    
        messages_data = json.load(f)
        return [Message(**data) for data in messages_data]


def save_message(message: Message):
    messages = load_messages()
    messages.append(message)
    save_messages(messages)


def save_messages(messages: List[Message]):
    with open(path, 'w') as f:
        json.dump([message.dict() for message in messages], f)
