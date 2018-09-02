""" Card deck program.
"""

import collections
import itertools


deck = collections.namedtuple('deck', 'rank suit')
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck(object):
    """ Deck of cards.
    """
    ranks = [str(rank) for rank in range(2, 11)] + list('JQKA')
    suit = ['spades', 'diamonds', 'hearts', 'clubs']

    def __init__(self):
        self.cards = [
            deck(rank, suit)
            for rank, suit in itertools.product(self.ranks, self.suit)
        ]

    def __getitem__(self, position):
        """ Make the object iterable and search by index.
        """
        return self.cards[position]

    def __len__(self):
        """ Get the length of the deck.
        """
        return len(self.cards)

    def __repr__(self):
        """ Represent the object.
        """
        return "{classname}()".format(classname=self.__class__.__name__)



def spadesHigh(card):
    """ Filter spades.
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    deckOfCards = FrenchDeck()
    print(sorted(deckOfCards, key=spadesHigh))