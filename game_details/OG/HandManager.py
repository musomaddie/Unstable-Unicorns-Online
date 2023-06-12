class HandManager:
    """ Managers the hand of the player. Responsible for handling actions
    related to the hand.

    Paramaters:
        player (player): the player whose hand this is.
        cards (List<Card>): all the cards currently in the hand.
    """

    def __init__(self, player=None, cards=[]):
        self.player = player
        self.cards = cards

    def __repr__(self):
        return f"The hand manager for {self.player.name} containing: " \
               f"{' '.join(self.cards)}"
