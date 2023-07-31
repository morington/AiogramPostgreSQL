import logging
from typing import NoReturn, Any, Union
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.engine import ScalarResult
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import (
    NoResultFound,
)

from src.tgbot.models import User

logger = logging.getLogger(__name__)


class DataAccessObject:
    def __init__(self, session: AsyncSession) -> NoReturn:
        self.session: AsyncSession = session

    #  Get object from id
    async def get_object(
        self, db_object: Union[User], db_object_id: int = None
    ) -> list:
        stmt = select(db_object)
        if db_object_id:
            stmt = stmt.where(db_object.id == db_object_id)

        result: ScalarResult = await self.session.execute(stmt)
        return [item.to_dict for item in result.scalars().all()]

    #  Merge object
    async def add_object(
        self,
        db_object: Union[User],
    ) -> None:
        await self.session.merge(db_object)
