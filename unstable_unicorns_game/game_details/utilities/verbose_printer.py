from unstable_unicorns_game.game_details.card import MultipleCardsHolder


class VerbosePrinter:
    """ Prints things but only if verbose is enabled. """

    def __init__(self, verbose: bool):
        self.enabled = verbose

    def print(self, message: str):
        if self.enabled:
            print(message)

    @staticmethod
    def create_card_names_str(cards: MultipleCardsHolder) -> str:
        return ", ".join([card.name for card in cards])
