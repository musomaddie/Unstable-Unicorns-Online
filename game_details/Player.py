class Player:

    def __init__(self, name, baby):
        self.name = name
        self.hand = []
        self.stable = [baby]
        self.num_unicorns = 1

    def add_card(self, card):
        self.hand.append(card)

    def __repr__(self):
        return f"This is player {self.name} their cards are: {self.hand}"
