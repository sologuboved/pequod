import random
import json


TITLE = 'title'
TEXT = 'text'


def load_json(json_filename):
    with open(json_filename) as data:
        return json.load(data)


def get_random_extract():
    random_extract = load_json('/home/sologuboved/scripts/mobydick/extracts/extracts.json')[random.randrange(0, 80)]
    return random_extract[TITLE], random_extract[TEXT]


def get_random_paragraph():
    chapter = load_json('/home/sologuboved/scripts/mobydick/mobydick_json/{}.json'.format(random.randint(1, 136)))
    title = chapter[TITLE]
    text = chapter[TEXT]
    paragraph = text[random.randrange(0, len(text))]
    return title, paragraph
