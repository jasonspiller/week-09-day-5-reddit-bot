"""
Simple reddit bot that looks for mentions of my focus characters.

When detected, it comments with a simple message and a link to
their profile on a community resource.

Created by: Jason Spiller
License: MIT
"""

import praw
import os
import time
import re

"""
List of favorite characters from Star Wars, Transformers, G.I. Joe, and
Masters of the Universe and their corresponding profile links.
"""
CHARACTERS = {
    'Royal Guard':  'http://starwars.wikia.com/wiki/Emperor%27s_Royal_Guard',
    'IG-88':        'http://starwars.wikia.com/wiki/IG-88',
    'Ultra Magnus': 'https://tfwiki.net/wiki/Soundwave_(G1)',
    'Soundwave':    'https://tfwiki.net/wiki/Ultra_Magnus_(G1)',
    'Mainframe':    'http://gijoe.wikia.com/wiki/Mainframe_(RAH)',
    'Storm Shadow': 'http://gijoe.wikia.com/wiki/Storm_Shadow_(RAH)',
    'Hordak':       'http://www.he-man.org/encyclopedia/viewobject.php?cat=3&objectid=291',
    'Trap Jaw':     'http://www.he-man.org/encyclopedia/viewobject.php?cat=3&objectid=285'
}

SUBS = [
    'ActionFigures',
    'transformers',
    'StarWars',
    'gijoe',
    'MastersOfTheUniverse'
]

# file that keeps track of the submission the bot has posted in
PATH = '/Users/jasonspiller/Dropbox/projects/WDI/homework/week-09/day-5-reddit-bot/commented.txt'


class RedditBot():
    """reddit bot."""

    def __init__(self, characters, subs, path):
        """Initialize the bot."""
        print("Initializing Bot")

        # access to settings (character, subs and path)
        self.characters = characters
        self.subs = subs
        self.path = path

        self.main()

    def authenticate(self):
        """Sign in to reddit."""
        print('Signing In...\n')
        reddit = praw.Reddit(
            'FocusCharacterBot', user_agent='web:FocusCharacterBot:v0.1 (by \
            u/slickmcfav)')
        print('Authenticated as {}\n'.format(reddit.user.me()))
        return reddit

    def run_bot(self, reddit):
        """Run the bot."""
        print('Getting 100 posts. \n')

        # this will output subs when ready for production: '+'.join(self.subs)
        for submission in reddit.subreddit('test').new(limit=100):

            for key, value in self.characters.items():

                match = re.findall(key, submission.selftext)

                if match:
                    print(key + ' found in submission ID: ' + submission.id)

                    if not os.path.exists(self.path):
                        open(self.path, 'w').close()

                    file_obj_r = open(self.path, 'r')

                    if submission.id not in file_obj_r.read().splitlines():
                        print('Link is unique. Creating and posting comment. \n')

                        # comment content
                        header = 'This is one of my creator\'s favorite characters. \n\n'
                        body = 'I have let him you you guys are talking about ' + key + '. If you would \
                        like to know more about ' + key + ', please see the lnk below. \n\n \
                        [' + value + '](' + value + ') \n\n'
                        footer = '| Posted by FocusCharacterBot | Bot created by u/slickmcfav |'

                        submission.reply(header + body + footer)

                        file_obj_r.close()

                        file_obj_w = open(self.path, 'a+')
                        file_obj_w.write(submission.id + '\n')
                        file_obj_w.close()
                    else:
                        print('Already replied to submission. No reply needed. \n')

                    time.sleep(10)

        print('Waiting 60 seconds. \n')
        time.sleep(60)

    def main(self):
        """Launch the app."""
        reddit = self.authenticate()
        while True:
            self.run_bot(reddit)


bot = RedditBot(CHARACTERS, SUBS, PATH)
