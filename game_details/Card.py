class Card:

    def __init__(self, result):
        self.name = result[1]
        self.card_type = result[2]
        self.text = result[3]
        self.action_on_enter = result[4] == "TRUE"
        self.action_on_start = result[5] == "TRUE"
        self.discard_action = result[6]
        self.stable_effect = result[7] == "TRUE"
        self.search_deck = result[8]
        self.shuffle_deck = result[9] == "TRUE"
        self.shuffle_discard = result[10] == "TRUE"
        self.scarifice_action = result[11]
        self.return_to_hand = result[12] == "TRUE"
        self.search_discard = result[13]
        self.protection = result[14]
        self.draw_action = result[15]
        self.destroy_action = result[16]
        self.requires_basic = result[17] == "TRUE"
        self.action_on_leave = result[18] == "TRUE"

        # Default if false any effect will not be triggered
        self.effect_will_be_triggered = True

    def in_dict(self, dictionary):
        return self.name in dictionary

    def is_magic_type(self):
        return self.card_type == "Magic"

    def is_match(self, matching_type, matching_term, exact_match):
        value = None
        if matching_type == "name":
            value = self.name

        # Quit early if nothing assigned
        if not value:
            return False

        # Check the term
        if exact_match:
            return value == matching_term

    def is_unicorn(self):
        return "Unicorn" in self.card_type

    def restore_defaults(self):
        # Restore any default values
        self.effect_will_be_triggered = True

    def __str__(self):
        return f"{self.name} (card)"

    def __repr__(self):
        return f"{self.name} (card)"

    def __eq__(self, other):
        return self.name == other.name
