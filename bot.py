import asyncio
import random

from telegram import Bot

from get_random_passage import get_random_extract, get_random_paragraph
from pid_ops import write_pid
from userinfo import TOKEN


def main():
    if random.randrange(20):
        extractor = get_random_paragraph
    else:
        extractor = get_random_extract
    title, passage = extractor()
    text = title + '\n\n' + passage
    print(text)
    asyncio.run(Bot(token=TOKEN).send_message(chat_id='@green_hand_at_whaling', text=text))


if __name__ == '__main__':
    write_pid()
    main()
