import asyncio
import os
from src import start_app


if __name__ == "__main__":
    configfile = os.environ.get("CONFIG", "bot.ini")

    try:
        asyncio.run(start_app(configfile))
    except (KeyboardInterrupt, SystemError):
        print("-> Bot stopped!")
