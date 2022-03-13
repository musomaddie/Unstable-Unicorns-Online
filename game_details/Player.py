class Player:
    """ Represents a player in the game.

    Parameters:
        name (str): the players name
        hand (HandManager): controls the state of the players hand.
        stable (StableManager): controls the players stable.
    """

    def __init__(self, name):
        self.name = name
        self.hand = [] # TODO: update when HandManager is created.
        self.stable = [] # TODO: update when StableManager is created.

    def __repr__(self):
        return f"{self.name} (player)"
