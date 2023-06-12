class StableManager:
    """ Represents a players stable. Responsible for managing all interactions
    with it.

    Parameters:
        player (Player): the player whose stable it is
        unicorns (list<Card>): the unicorns currently in the stable
        upgrades (list<Card>): the upgrades currently in the stable
        downgrades (list<Card>): the downgrades currently in the stableA
    """

    def __init__(self, player=None, unicorns=[], upgrades=[], downgrades=[]):
        self.player = player
        self.unicorns = unicorns
        self.upgrades = upgrades
        self.downgrades = downgrades
