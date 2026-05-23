import logging
import threading
import os

from .utubebot import UtubeBot
from .config import Config


def run_web():
    os.system("python web.py")


if __name__ == "__main__":
    threading.Thread(target=run_web).start()

    logging.basicConfig(
        level=logging.DEBUG if Config.DEBUG else logging.INFO
    )

    logging.getLogger("pyrogram").setLevel(
        logging.INFO if Config.DEBUG else logging.WARNING
    )

    UtubeBot().run()
