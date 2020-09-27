import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("game_details")])
from game_details.CardLocation import CardLocation


class Player:

    def __init__(self, name, baby):
        self.name = name
        self.hand = []
        self.stable = [baby]
        self.num_unicorns = 1
        self.barbed_wire_effect = False  # Downgrade
        self.unicorn_destroy_decoy = False  # Upgrade
        self.unicorn_effects_blocked = False  # Downgrade
        self.unicorn_sacrifice_decoy = False  # Upgrade
        self.share_upgrades = False  # Downgrade
        self.protected_from_unicorn = False  # Upgrade
        self.protected_from_dragons = False  # Upgrade
        self.downgrades_have_no_effect = False  # Upgrade

    def add_to_hand(self, card):
        card.location = CardLocation.HAND
        self.hand.append(card)

    def add_to_stable(self, card):
        card.location = CardLocation.STABLE
        if card.is_unicorn():
            self.num_unicorns += 1
        self.stable.append(card)

    def get_downgrades(self):
        return [card for card in self.stable if card.is_downgrade()]

    def get_stable_modifiers(self):
        return [card for card in self.stable if not card.is_unicorn()]

    def get_unicorns(self):
        return [card for card in self.stable if card.is_unicorn()]

    def get_upgrades(self):
        return [card for card in self.stable if card.is_upgrade()]

    def has_won(self, win_num):
        return len(self.stable) >= win_num

    # Identifies which card to play :)
    def play_card(self, card_num):
        return self.hand.pop(card_num)

    def remove_card_from_hand(self, card_to_remove):
        index = 0
        for card in self.hand:
            if card == card_to_remove:
                break
            index += 1
        if index >= len(self.hand):
            raise LookupError("The card is not found in the hand")
        return self.hand.pop(index)

    def remove_card_from_stable(self, card_to_remove):
        # Find the card
        index = 0
        for card in self.stable:
            if card == card_to_remove:
                break
            index += 1

        # Sanity check the input size
        if index >= len(self.stable):
            raise LookupError("The unicorn does not exist in the given stable")
        # Change number if appropriate
        if card_to_remove.is_unicorn():
            self.num_unicorns -= 1
        return self.stable.pop(index)

    def sacrifice_instead(self):
        if self.unicorn_destroy_decoy or self.unicorn_sacrifice_decoy:
            # Looking for black Knight or Blow Up Unicorn
            index = 0
            for card in self.stable:
                if (card.name == "Black Knight Unicorn"
                    or card.name == "Blow Up Unicorn"):
                    break
                index += 1
            return self.stable[index]

    def __eq__(self, other):
        # Trying to be fancy and allow comparison just using plain strings
        if isinstance(other, Player):
            return self.name == other.name
        return False

    def __repr__(self):
        return f"This is player {self.name} their cards are: {self.hand}"
