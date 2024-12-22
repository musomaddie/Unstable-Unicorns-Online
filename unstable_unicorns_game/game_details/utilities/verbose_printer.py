from unstable_unicorns_game.game_details.card import MultipleCardsHolder


class VerbosePrinter:
    """ Prints things but only if verbose is enabled. """

    def __init__(self, verbose: bool):
        self.enabled = verbose
        self._prefix = ""

    def print(self, message: str):
        if self.enabled:
            print(f"{self._prefix}{message}")

    def extend_prefix(self):
        self._prefix += "\t"

    def unextend_prefix(self):
        self._prefix = self._prefix[:-2]

    @staticmethod
    def create_card_names_str(cards: MultipleCardsHolder) -> str:
        return ", ".join([card.name for card in cards])
