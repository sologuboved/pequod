import json
import random


def load_json(json_filename):
    with open(json_filename) as data:
        return json.load(data)


def get_random_extract():
    random_extract = load_json(
        '/home/sologuboved/scripts/mobydick_sources/extracts/extracts.json',
    )[random.randrange(0, 80)]
    return random_extract['title'], random_extract['text']


def get_random_paragraph():
    chapter = load_json(f'/home/sologuboved/scripts/mobydick_sources/mobydick_json/{random.randint(1, 136)}.json')
    text = chapter['text']
    paragraph = text[random.randrange(0, len(text))]
    return chapter['title'], paragraph
