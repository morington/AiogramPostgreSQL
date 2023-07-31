import logging

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from src.tgbot.config.config import DbConfig

logger = logging.getLogger(__name__)


Base = declarative_base()


async def create_async_engine_db(
    config: DbConfig,
    echo: bool,
) -> AsyncEngine:
    return create_async_engine(config.conn(), echo=echo)


async def async_connection_db(
    engine: AsyncEngine,
    expire_on_commit: bool,
) -> AsyncSession:
    return async_sessionmaker(engine, expire_on_commit=expire_on_commit)
