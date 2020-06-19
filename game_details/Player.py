class Player:

    def __init__(self, name, baby):
        self.name = name
        self.hand = []
        self.stable = [baby]
        self.num_unicorns = 1
        self.barbed_wire_effect = False
        self.unicorn_destroy_decoy = False

    def add_to_hand(self, card):
        self.hand.append(card)

    def add_to_stable(self, card):
        if card.is_unicorn():
            self.num_unicorns += 1
        self.stable.append(card)

    def get_unicorns(self):
        return [card for card in self.stable if card.is_unicorn()]

    def has_won(self, win_num):
        return len(self.stable) >= win_num

    # Identifies which card to play :)
    def play_card(self, card_num):
        return self.hand.pop(card_num)

    def remove_card_from_stable(self, card_to_remove):
        # Find the card
        index = 0
        for card in self.stable:
            if card == card_to_remove:
                break
            index += 1
        # Change number if appropriate
        if card_to_remove.is_unicorn():
            self.num_unicorns -= 1
        return self.stable.pop(index)

    def sacrifice_instead(self):
        if self.unicorn_destroy_decoy:
            # Looking for black Knight
            index = 0
            for card in self.stable:
                if card.name == "Black Knight Unicorn":
                    break
                index += 1
            return self.stable[index]

    def __repr__(self):
        return f"This is player {self.name} their cards are: {self.hand}"
