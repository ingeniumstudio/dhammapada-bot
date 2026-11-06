#!/usr/bin/env python

import datetime
import os
import json
import random

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True if os.environ.get('DEBUG') else False  # not implemented tho

# This file contains The Dhamapada in JSON format
DHAMMAPADA_JSON_FILEPATH = f"{SCRIPT_PATH}/dhammapada.json"

# This file contains the currently (last) posted verse
VERSE_FILEPATH = os.path.expanduser("~/.dhammapada-bot.txt")

#  FORMAT_LOCAL = """\
#  {verse}
#
#  {signature:>{line_size}}
#  {date:>{line_size}}\
#  """
FORMAT_LOCAL = """\
{verse}

{signature}
{date}\
"""


def print_debug(bot):

    print("message_local", bot.formatted_texts['local'], sep="\n\n",
          end="\n\n")


class DhammapadaBot:

    def __init__(self):
        pass

    def get_random_verse(self):

        verse_numbers, verse = self.get_verse()
        verses = str(", ").join([str(verse_number)
                                 for verse_number in verse_numbers])
        signature = f"— Lord Buddha; Dhammapada {verses}"

        self.verse = verse
        self.verse_numbers = verse_numbers
        self.signature = signature

    def format_texts(self):

        formatted_date_time = datetime.datetime.now().strftime("%a %b %d %Y, "
                                                               "%I:%M:%S%p "
                                                               "GMT-3")
        date = f"[{formatted_date_time}]"

        verse = self.verse
        signature = self.signature

        #  line_size = self.text_width(text=verse)

        #  message_local = FORMAT_LOCAL.format(verse=verse,
        #                                      signature=signature,
        #                                      date=date,
        #                                      line_size=line_size)
        message_local = FORMAT_LOCAL.format(verse=verse,
                                            signature=signature,
                                            date=date)

        formatted_texts = {
                "local": message_local,
                }
        self.formatted_texts = formatted_texts

    def write_verse_to_local_file(self, verse_file=VERSE_FILEPATH):
        """Writes the current verse being posted to the file in
               `VERSE_FILEPATH`
        """

        verse = self.formatted_texts['local']

        with open(verse_file, "w") as fd:
            fd.write(verse)

    def get_verse(self):
        """Gets a random verse from The Dhammapada, from the file in
               `DHAMMAPADA_JSON_FILEPATH`
        """

        with open(DHAMMAPADA_JSON_FILEPATH, "r") as dhammapada_json_file:
            dhammapada_json = json.load(dhammapada_json_file)

        keys = dhammapada_json.keys()
        random_choice = random.choice(list(keys))

        return dhammapada_json[random_choice]

    #  def text_width(self, text):
    #      """Iterates over all the lines of the verse and return the number
    #             of characters from the lenghtiest line; used for formatting
    #      """
    #
    #      lines = text.split('\n')
    #      lenghtiest_line = max(map(len, lines))
    #
    #      return lenghtiest_line

    def print_verse(self):

        verse = self.formatted_texts['local']

        print(verse)


if __name__ == "__main__":

    bot = DhammapadaBot()

    bot.get_random_verse()
    bot.format_texts()

    if DEBUG:
        bot.print_verse()
        exit(0)

    bot.write_verse_to_local_file()

