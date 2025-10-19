""" Differs from the printer by saving this to an external file with the intention of it being analysed later. """
import json

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.game.player.stable import Stable

# List of all dictionary keys here ....
folder = "logs"
S_INFO = "starting info"

N_PLAYERS = "number of players"
PLAYER_NAMES = "player names"
PLAYER_IDYS = "identifiers"
# TODO -> remove the numeric identifier from the name once duplicate names are disallowed.
PLAYER_DETS = "player details"

K_HAND = "hand"
K_STABLE = "stable"
K_UNICORNS = "unicorns"
K_UPGRADES = "upgrades"
K_DOWNGRADES = "downgrades"


class Logger:
    """ Saves a json log summarising the game with the intention of it being analyzed. """

    # TODO -> consider moving the logging details into the classes themselves. The logger can (if needed) call those
    #  log methods. (make this like verbose_printer.

    def __init__(self, enabled: bool = True):
        self._enabled = enabled
        # TODO -> dynamically determine the file naming.
        self.filename = f"{folder}/game_00.json"

    def game_creation(self, game: 'Game'):
        if not self._enabled:
            return
        player_dict = {
            N_PLAYERS: len(game.players),
            PLAYER_NAMES: [player.name for player in game.players],
            PLAYER_IDYS: [Logger.make_player_identifier(index, player) for index, player in enumerate(game.players)],
        }
        overall_dict = {
            PLAYER_DETS: player_dict,
            S_INFO: [
                {
                    Logger.make_player_identifier(index, player): Logger.log_player(player)
                } for index, player in enumerate(game.players)
            ]
        }

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(
                overall_dict, f, ensure_ascii=False, indent=4
            )

    @staticmethod
    def make_player_identifier(index, player):
        return f"{index}_{player.name}"

    @staticmethod
    def log_card(card: Card) -> str:
        # TODO -> update what we store here -> probably minimal info to avoid bloat, since we can look up the
        #  unicorns in the original dict regardless.
        # TODO -> make an identifier for the cards (i.e. for those who just have a diff image vs name) and use that
        #  here instead.
        return card.name

    @staticmethod
    def log_player(player: Player) -> dict:
        return {
            K_HAND: Logger.log_hand(player.hand),
            K_STABLE: Logger.log_stable(player.stable)
        }

    @staticmethod
    def log_stable(stable: Stable) -> dict:
        # Always log the unicorns:
        result = {K_UNICORNS: [Logger.log_card(card) for card in stable.unicorns]}

        def log_if_non_zero(cards: MultipleCardsHolder, key: str):
            if len(cards) == 0:
                return
            result[key] = [Logger.log_card(card) for card in cards]

        log_if_non_zero(stable.upgrades, K_UPGRADES)
        log_if_non_zero(stable.downgrades, K_DOWNGRADES)

        return result

    @staticmethod
    def log_hand(hand: Hand) -> list:
        return [Logger.log_card(card) for card in hand]
