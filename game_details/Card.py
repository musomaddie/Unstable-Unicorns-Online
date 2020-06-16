class Card:

    def __init__(self, result):
        self.name = result[1]
        self.card_type = result[2]
        self.text = result[3]
        self.action_on_enter = result[4]
        self.discard_action = result[5]
        self.stable_effect = result[6]
        self.search_deck = result[7]
        self.shuffle_deck = result[8]
        self.shuffle_discard = result[9]
        self.scarifice_action = result[10]
        self.return_to_hand = result[11]
        self.search_discard = result[12]
        self.protection = result[13]
        self.draw_action = result[14]
        self.destroy_action = result[15]
        self.requires_basic = result[16]
        self.action_on_leave = result[17]

        # Default if false any effect will not be triggered
        self.effect_will_be_triggered = True

    def restore_defaults(self):
        # Restore any default values
        self.effect_will_be_triggered = True

    def is_magic_type(self):
        return self.card_type == "Magic"

    def in_dict(self, dictionary):
        return self.name in dictionary

    def is_unicorn(self):
        return "Unicorn" in self.card_type

    def __str__(self):
        return f"Card is {self.name}"

    def __repr__(self):
        return "card is " + self.name

    def __eq__(self, other):
        return self.name == other.name
