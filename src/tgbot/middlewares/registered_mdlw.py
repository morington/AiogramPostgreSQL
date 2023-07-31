import logging
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject, user

from sqlalchemy import select
from sqlalchemy.engine import ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from src.tgbot.models import User
from src.tgbot.services.data_access_object import DataAccessObject


logger = logging.getLogger(__name__)


class RegisteredMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        tg_user: user.User = data.get("event_from_user")
        dao: DataAccessObject = data["dao"]

        if not await dao.get_object(User, tg_user.id):
            await dao.add_object(
                User(
                    id=tg_user.id,
                    fullname=tg_user.full_name,
                    username=tg_user.username,
                )
            )

        return await handler(event, data)
