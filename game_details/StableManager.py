import os
import sys

sys.path.insert(0, 
        os.path.dirname(os.path.realpath(__file__))[
            0:-len("game_details")])

from game_details.Card import CardType


class StableManager:
    """ Represents a players stable. Responsible for managing all interactions
    with it.

    Parameters:
        player (Player): the player whose stable it is
        unicorns (list<Card>): the unicorns currently in the stable
        upgrades (list<Card>): the upgrades currently in the stable
        downgrades (list<Card>): the downgrades currently in the stableA

    Methods:
        add_card(card): adds the given card to the stable.
    """

    def __init__(self, player):
        self.player = player
        self.unicorns = []
        self.upgrades = []
        self.downgrades = []

    def __repr__(self):
        return f"Stable Manager contains {len(self.unicorns)} unicorns for {self.player}"

    def add_card(self, card):
        """ Adds the given card to the stable.

        Parameters:
            card (Card): the card to add.
        """
        print(f"SM adding {card} for {self.player}")
        if (card.card_type == CardType.UPGRADE):
            self.upgrades.append(card)
        elif (card.card_type == CardType.DOWNGRADE):
            self.downgrades.append(card)
        else:
            self.unicorns.append(card)
