from telegram.ext import Updater, CommandHandler
from tkn import TOKEN

updater = Updater(token=TOKEN)
job_queue = updater.job_queue


def callback_minute(bot, job):
    bot.send_message(chat_id='@green_hand_at_whaling',
                     text="One message every 30 seconds")


job_queue.run_repeating(callback_minute, interval=30, first=0)

updater.start_polling()
