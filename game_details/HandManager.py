class HandManager:
    """ Managers the hand of the player. Responsible for handling actions
    related to the hand.

    Paramaters:
        player (player): the player whose hand this is.
        cards (List<Card>): all the cards currently in the hand.

    Methods:
        add_card(card): adds the given card to the hand.
    """

    def __init__(self, player):
        self.player = player
        self.cards = []

    def __repr__(self):
        return f"Hand manager for {self.player.name}"

    def add_card(self, card):
        """ Adds the given card to the end of the hand.

        Parameters:
            card (Card): the card to add.
        """
        self.cards.append(card)
