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

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
