from aiogram import Router, F
from aiogram.filters import Command, CommandStart


from .start import command_start


router: Router = Router(name=__name__)
router.message.filter(F.chat.type == "private")
router.message.register(command_start, CommandStart())
