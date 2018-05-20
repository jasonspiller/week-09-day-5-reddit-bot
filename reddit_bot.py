"""
Simple reddit bot that looks for mentions of my focus characters.

When detected, it comments with a simple message and a link to
their profile on a community resource.

Created by: Jason Spiller
License: MIT
"""

from bs4 import BeautifulSoup
from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4


"""
List of favorite characters from Star Wars, Transformers, G.I. Joe, and Masters
of the Universe and their corresponding profile links.
"""
dicCharacters = {
    'Royal Guard':  'http://starwars.wikia.com/wiki/Emperor%27s_Royal_Guard',
    'IG-88':        'http://starwars.wikia.com/wiki/IG-88',
    'Ultra Magnus': 'https://tfwiki.net/wiki/Soundwave_(G1)',
    'Soundwave':    'https://tfwiki.net/wiki/Ultra_Magnus_(G1)',
    'Mainframe':    'http://gijoe.wikia.com/wiki/Mainframe_(RAH)',
    'Storm Shadow': 'http://gijoe.wikia.com/wiki/Storm_Shadow_(RAH)',
    'Hordak':       'http://www.he-man.org/encyclopedia/viewobject.php?cat=3&objectid=291',
    'Trap Jaw':     'http://www.he-man.org/encyclopedia/viewobject.php?cat=3&objectid=285'
}

# file that keeps track of where the bot has posted
path = '/Users/jasonspiller/Dropbox/projects/WDI/homework/week-09/day-5-reddit \
        -bot/commented.txt'

# comment content
header = 'This is one of my creator\'s favorite characters.'
body = 'I have let him you you guys are talking about [BLANK]. If you would like \
to know more about [BLANK], please see the lnk below. \
\n\n [LINK]'
footer = '\n\n| Posted by FocusCharacterBot | Bot created by u/slickmcfav |'


class RedditBot():
    """reddit bot."""

    def __init__(self, characters):
        """So you say you need a comment."""

    def authenticate():
        """Sign in to reddit."""
        print('Signing In...\n')
        reddit = praw.Reddit(
            'FocusCharacterBot', user_agent='web:xkcd-explain-bot:v0.1 (by \
            u/slickmcfav)')
        print('Authenticated as {}\n'.format(reddit.user.me()))
        return reddit


bot = RedditBot(dicCharacters)
