class Card:

    def __init__(self, name, card_type, text,
                 action_on_enter,
                 action_on_begin,
                 discard_action,
                 stable_effect,
                 search_deck,
                 shuffle_deck,
                 shuffle_discard,
                 scarifice_action,
                 return_to_hand,
                 search_discard,
                 protection,
                 draw_action,
                 destroy_action,
                 requires_basic,
                 action_on_leave):
        self.name = name
        self.card_type = card_type
        self.text = text
        self.action_on_enter = action_on_enter
        self.discard_action = discard_action
        self.stable_effect = stable_effect
        self.search_deck = search_deck
        self.shuffle_deck = shuffle_deck
        self.shuffle_discard = shuffle_discard
        self.scarifice_action = scarifice_action
        self.return_to_hand = return_to_hand
        self.search_discard = search_discard
        self.protection = protection
        self.draw_action = draw_action
        self.destroy_action = destroy_action
        self.requires_basic = requires_basic
        self.action_on_leave = action_on_leave
