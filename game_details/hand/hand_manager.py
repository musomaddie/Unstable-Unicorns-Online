from game_details.hand import Hand


class HandManager:
    """ Manages the hand. """

    def __init__(self, hand=Hand):
        self.hand = hand
