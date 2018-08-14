import datetime
from telegram.ext import Updater
from tkn import TOKEN
from get_random_passage import *


def random_quoter(bot, job):
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
    job_queue = updater.job_queue
    job_queue.run_daily(random_quoter, time=datetime.time(17, 00))
    # job_queue.run_repeating(another_func, datetime.timedelta(hours=3.0), first=0)
    updater.start_polling()
