"""
Simple reddit bot that looks for mentions of my focus characters.

When detected, it comments with a simple message and a link to
their profile on a community resource.
"""


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


class RedditBot():
    """reddit bot."""

    def __init__(self, characters):
        """So you say you need a comment."""
        self.dict_states = {}
        self.stats = {'Correct': 0, 'Incorrect': 0}
        self.shuffle_states(characters)
        self.instructions()
        self.play_game()
        self.play_again()


bot = RedditBot(dicCharacters)
