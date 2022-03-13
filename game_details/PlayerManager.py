class PlayerManager:
    """ A class to manage all the players. All the interactions a player has
    should be managed here.

    Parameters:
        players (list<Player): all the existing players.
    """

    def __init__(self, players):
        self.players = players

    def __repr__(self):
        return f"Player manager of {self.players}"
