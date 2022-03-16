import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("game_details")])

from game_details.PlayerManager import PlayerManager


class PlayersManager:
    """ A class to manage all the players. All the interactions a player has
    should be managed here.

    Parameters:
        players (list<Player): all the existing players.

    Methods:
        all_players(): returns all the players.
        find_player_from_index(i): returns the player at the given index
        prepare_game_start(nursery, deck): does all
            the pregame actions for each player.
    """

    def __init__(self, player_names):
        self.players = [PlayerManager(name) for name in player_names]

    def __repr__(self):
        return f"Players manager with {len(self.players)} players"

    def all_players(self):
        """ Returns a list of all the players.

        Returns:
            list<PlayerManager>: all the players.
        """
        return self.players

    def find_player_from_index(self, i):
        """ Returns the player that is found at the given index.

        Parameters:
            i (int): the index we need the player from

        Returns:
            PlayerManager: the player at that position.

        TODO: should complain if out of bounds
        """
        return self.players[i]

    def prepare_game_start(self, nursery, deck):
        """ Prepares each player for the start of the game.
        This involves assigning everyone a baby unicorn from the nursery and 5
        cards from the deck. 

        Parameters:
            nursery (NurseryManager): the nursery
            deck (DeckManager): the deck
        """
        # Everyone needs a baby.
        [player.add_baby(nursery) for player in self.players]

        # Everyone needs 5 cards from the deck.
        [[player.add_to_hand(deck.draw_top_card()) for player in self.players ]
            for _ in range(5)]
