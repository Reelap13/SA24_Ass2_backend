from fastapi import APIRouter
from config import settings

from .chat import router as messages_router

router = APIRouter()

router.include_router(router=messages_router, prefix=settings.api.messages)
