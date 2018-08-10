import datetime
from telegram.ext import Updater
from tkn import TOKEN
from get_random_passage import *


def callback_func(bot, job):
    if random.randrange(10):
        extractor = get_random_paragraph
    else:
        extractor = get_random_extract
    bot.send_message(chat_id='@green_hand_at_whaling',
                     text=get_message(extractor))


def get_message(extractor):
    title, passage = extractor()
    return title + '\n\n' + passage


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    updater.job_queue.run_daily(callback_func, time=datetime.time(17, 0))
    # updater.job_queue.run_repeating(callback_func, interval=30, first=0)
    updater.start_polling()
