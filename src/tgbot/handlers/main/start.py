import logging

from aiogram.types import Message


logger = logging.getLogger(__name__)


async def command_start(message: Message) -> None:
    await message.answer(
        text="Hello World",
        reply_markup=None,
    )
