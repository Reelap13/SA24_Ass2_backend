from schemas.chat_scheme import (
    SendMessageScheme,
)

from systems.chat_system import chat, Message 


async def send_message(message: SendMessageScheme) -> dict:

    await chat.add_message(Message(**message.dict()))

    return {'message': 'Message was sent'}


async def get_messages() -> dict:
    
    messages = await chat.get_messages()
    
    return {'messages': f'{messages}'}


async def get_messages_count() -> dict:

    count = await chat.get_messages_count()

    return {'count': f'{count}'}