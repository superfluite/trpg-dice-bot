import random

from telegram import Bot
from telegram.ext import Updater, CommandHandler


class TelegramBot:
    def __init__(self, name: str, token: str):
        self.core = Bot(token)
        self.updater = Updater(token)
        self.name = name

    def sendMessage(self, chat_id, text):
        self.core.sendMessage(chat_id=chat_id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()


class DiceBot(TelegramBot):
    def __init__(self):
        self.token = '779460584:AAGtNjvinoWe449nnzvHe1pdlRj_ulzd5ak'
        super(DiceBot, self).__init__('dice_bot', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.updater.start_polling()
        self.updater.idle()


class Dice:
    def __init__(self, cnt: int, upper: int):
        self.cnt = cnt
        self.upper = upper

    def roll(self):
        results = []
        for i in range(0, self.cnt):
            results.append(random.randint(1, self.upper))
        return results
