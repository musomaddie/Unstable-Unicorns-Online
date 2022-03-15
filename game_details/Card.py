from enum import auto
from enum import Enum

class Card:

    """ Represents a card in the game.

    Parameters:
        name (string): the name
        card_type (CardType): the type
        text (string): the text on the card
        action_on_enter (bool): true if the card triggers an action entering a stable
        action_on_begin (bool): true if the card either requires or allows the
            possibility of an action at the start of a turn
        discard_action (bool): true if the card requires something to be
            discarded.
        stable_effect (bool): true if the card has an effect on the stable
        search_deck (bool): true if the card allows the searching of the deck
        shuffle_deck (bool): true if the card requires the deck to be shuffled.
        shuffle_discard (bool): true if the card requires the discard pile to be
            shuffled into the deck.
        scarifice_action (bool): true if the card requires a scarifice
        return_to_hand (bool): true if the card requires another card to be
            returned to your hand.
        search_discard (bool): true if the card allows the discard pile to be
            searched.
        protection (bool): true if the card offers some protection
        draw_action (bool): true if the card allows another draw action
        destroy_action (bool): true if the card requires something to be
            destroyed
        requires_basic (bool): true if the card requires a basic unicorn to be
            in the stable before being played.
        action_on_leave (bool): true if the card requires an action as it leaves
            a stable.

        Methods:
            name_equals(str): checks if the name of the card matches the given
            string.
    """

    def __init__(self, 
                 name, 
                 card_type, 
                 text,
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

    def __repr__(self):
        return f"{self.name} - {self.card_type} (card)"

    def name_equals(self, name):
        """ Checks if the name of the card is the same as the name provided. Is
        case sensitive

        Parameters:
            name (str): the name we are checking against the card.
        Returns:
            bool: true if they are the same otherwise false
        """
        return self.name == name



class CardType(Enum):
    def create_enum_from_string(card_type_str):
        if card_type_str == "Magic":
            return CardType.MAGIC
        elif card_type_str == "Magic Unicorn":
            return CardType.MAGIC_UNICORN
        elif card_type_str == "Basic Unicorn":
            return CardType.BASIC_UNICORN
        elif card_type_str == "Upgrade":
            return CardType.UPGRADE
        elif card_type_str == "Downgrade":
            return CardType.DOWNGRADE
        elif card_type_str == "Instant":
            return CardType.INSTANT
        elif card_type_str == "Baby Unicorn":
            return CardType.BABY_UNICORN
        # This should never be reached
        else:
            print("No matching card type find")
            return None

    MAGIC = auto()
    MAGIC_UNICORN = auto()
    BASIC_UNICORN = auto()
    UPGRADE = auto()
    DOWNGRADE = auto()
    INSTANT = auto()
    BABY_UNICORN = auto()
