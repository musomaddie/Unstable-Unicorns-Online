class Player:

    def __init__(self, name, baby):
        self.name = name
        self.hand = []
        self.stable = [baby]
        self.num_unicorns = 1

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self, card_num):
        return self.hand.pop(card_num).play()

    def handle_beginning_turn_action(self):
        pass

    def handle_draw(self):
        pass

    def handle_end_turn(self):
        pass

    def __repr__(self):
        return f"This is player {self.name} their cards are: {self.hand}"
