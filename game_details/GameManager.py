""" create_new_game: starts the game """
class GameManager:
    """ Responsible for managing the overall state of the game.

    Parameters:
        deck (DeckManager): manages the deck.
        discard_pile (DiscardManager): manages the discard pile
        players (PlayerManager): manages all the players
        nursery (NuseryManager): manages the nursery (baby bois)

    Methods:
    """

    def __init__(self, deck, discard_pile, players, nursery):
        self.deck = deck
        self.discard_pile = discard_pile
        self.players = players
        self.nursery = nursery
