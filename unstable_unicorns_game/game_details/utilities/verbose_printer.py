from unstable_unicorns_game.game_details.card.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.game_details.game import Game
from unstable_unicorns_game.game_details.player import Player


class VerbosePrinter:
    """ Prints things but only if verbose is enabled. """

    def __init__(self):
        self._prefix = ""

    def print(self, message: str = ''):
        print(f"{self._prefix}{message}")

    def extend_prefix(self):
        self._prefix += "\t"

    def unextend_prefix(self):
        self._prefix = self._prefix[:-1]

    def player_creation(self, player: Player):
        self.print(f"{player.name}: ")
        self.extend_prefix()
        self.print(f"{'Hand ':<16} : {VerbosePrinter.create_card_names_str(player.hand)}")
        self.print(f"{'Stable ':<16} : ")
        self.extend_prefix()
        self.print(f"{'Unicorns ':<12} : {VerbosePrinter.create_card_names_str(player.stable.unicorns)}")
        self.print(f"{'Upgrades ':<12} : {VerbosePrinter.create_card_names_str(player.stable.upgrades)}")
        self.print(f"{'Downgrades ':<12} : {VerbosePrinter.create_card_names_str(player.stable.downgrades)}")
        self.unextend_prefix()
        self.unextend_prefix()
        print()

    def game_creation(self, game: Game):
        self.print("Created game with: ")
        self.extend_prefix()
        self.print(f"{'Deck of game':<18} : {len(game.deck)}")
        self.print(f"{'Nursery of size':<18} : {len(game.nursery)}")
        self.print()
        self.print(f"Created players:")
        self.extend_prefix()
        for player in game.players:
            self.player_creation(player)
        self.unextend_prefix()

    @staticmethod
    def create_card_names_str(cards: MultipleCardsHolder) -> str:
        return ", ".join([card.name for card in cards])
