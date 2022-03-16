import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("game_details")])

from game_details.Player import Player

class PlayerManager:
    """ Responsible for managing a single player. All player interactions should
    be handled through this. 

    Parameters:
        player (Player): the player being managed.

    Methods:
        add_baby(nursery): adds a baby from the nursery to the players stable.
        add_to_hand(card): adds the given card to the players hand.
        add_to_stable(card): adds the given card to the players stable.
        has_won(): checks if the player has won.
    """

    def __init__(self, player_name):
        self.player = Player(player_name)

    def __repr__(self):
        return f"Player manager for {self.player}"

    def add_baby(self, nursery):
        """ Adds a baby to this players stable. 
        The baby is currently taken off the top of the nursery, but this will
        change once visual elements are added.

        Parameters:
            nursery (NuseryManager): the current nursery
        """
        self.player.add_to_stable(nursery.remove_from_nursery())

    def add_to_hand(self, card):
        """ Adds the given card to the players hand. 

        Parameters:
            card (Card): the card to add to the hand.
        """
        self.player.add_to_hand(card)

    def add_to_stable(self, card):
        """ Adds the given card to the players stable.

        Parameters:
            card (Card): the card to add to the stable.
        """
        self.player.add_to_stable(card)

    def has_won(self):
        """ Returns true if the current player has won the game. The win
        condition is based on the number of unicorns.
        TODO: make the number required variable.

        Returns:
            bool: true if the player has won, false otherwise.
        """
        return self.player.has_won()
