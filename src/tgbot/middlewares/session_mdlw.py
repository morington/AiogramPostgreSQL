import logging
from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from sqlalchemy.ext.asyncio import AsyncSession

from src.tgbot.services.data_access_object import DataAccessObject


logger = logging.getLogger(__name__)


class SessionMiddleware(BaseMiddleware):
    def __init__(self, sessionmaker: AsyncSession):
        super().__init__()
        self.sessionmaker = sessionmaker

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        async with self.sessionmaker() as session:
            async with session.begin():
                data["dao"] = DataAccessObject(session)
                return await handler(event, data)
