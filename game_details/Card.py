class Card:

    def __init__(self, result):
        self.name = result[1]
        self.card_type = result[2]
        self.text = result[3]
        self.action_on_enter = result[4]
        self.action_on_start = result[5]
        self.discard_action = result[6]
        self.stable_effect = result[7]
        self.search_deck = result[8]
        self.shuffle_deck = result[9]
        self.shuffle_discard = result[10]
        self.scarifice_action = result[11]
        self.return_to_hand = result[12]
        self.search_discard = result[13]
        self.protection = result[14]
        self.draw_action = result[15]
        self.destroy_action = result[16]
        self.requires_basic = result[17]
        self.action_on_leave = result[18]

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
        return f"{self.name} (card)"

    def __eq__(self, other):
        return self.name == other.name
