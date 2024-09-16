from fastapi import APIRouter, Depends
from fastapi import Request

from services import chat_service
from schemas.chat_scheme import SendMessageScheme
from services.response_service import ResponseService

router = APIRouter(tags=["Messages"])

@router.post("/")
async def send_message(
    message: SendMessageScheme
):
    return await ResponseService.response(
        chat_service.send_message(message=message)
    )


@router.get("/")
async def get_messages(
    request: Request
):
    return await ResponseService.response(chat_service.get_messages())


@router.get("/count")
async def get_messages_count(
    request: Request
):
    return await ResponseService.response(chat_service.get_messages_count())