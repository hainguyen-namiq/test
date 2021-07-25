import random
from datetime import datetime
from time import gmtime
import string
from unidecode import unidecode
import os


import argparse

starting_label_phrase = "    - "
parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=int)
args = parser.parse_args()

unknown_examples = [
    "không có",
    "không nhớ",
    "quên rồi",
    "chưa có",
    "k có",
    "k nhớ",
]

gender_group = [
    "Anh",
    "Chi",
    "anh",
    "chị",
    "Tui",
    "tui",
    "Tao",
    "tao",
    "Mình",
    "minh",
    "Em",
    "em",
]
if args.mode == 0:  # Provide unknown
    f = open("./data/nlu/unknown.yml", "w")
    f.write("version: \"2.0\"\n")
    f.write("nlu:\n")

    f.write("- intent: unknown\n")
    f.write("  examples: |\n")

    for i in range(0,100):
        raw_sentence = starting_label_phrase + " " + \
                        random.choice(gender_group) + " " + \
                        random.choice(unknown_examples)


        a = random.randint(1,5)
        # raw_sentence = unidecode(raw_sentence)
        if a < 1:
            f.write(raw_sentence + "\n")
        elif a < 2:
            # no hyphen
            sentence = unidecode(raw_sentence) + "\n"
            f.write(sentence)
        elif a < 3:
            # Write lower
            sentence = raw_sentence.lower() + "\n"
            f.write(sentence)
        elif a < 4:
            # Write lower hyphen
            sentence = unidecode(raw_sentence).lower() + "\n"
            f.write(sentence)
        else:
            # add .
            sentence = raw_sentence + "." + "\n"
            f.write(sentence)

    for i in range(0,100):
        raw_sentence = starting_label_phrase + " " + \
                        random.choice(unknown_examples)

        a = random.randint(1, 5)
        # raw_sentence = unidecode(raw_sentence)
        if a < 1:
            f.write(raw_sentence + "\n")
        elif a < 2:
            # no hyphen
            sentence = unidecode(raw_sentence) + "\n"
            f.write(sentence)
        elif a < 3:
            # Write lower
            sentence = raw_sentence.lower() + "\n"
            f.write(sentence)
        elif a < 4:
            # Write lower hyphen
            sentence = unidecode(raw_sentence).lower() + "\n"
            f.write(sentence)
        else:
            # add .
            sentence = raw_sentence + "." + "\n"
            f.write(sentence)