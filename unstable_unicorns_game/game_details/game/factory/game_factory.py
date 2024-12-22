""" factory for creating Game instances. """
from unstable_unicorns_game.game_details.card.factory import card_factory
from unstable_unicorns_game.game_details.deck.factory import deck_factory
from unstable_unicorns_game.game_details.discard_pile.factory import discard_pile_factory
from unstable_unicorns_game.game_details.game.game import Game
from unstable_unicorns_game.game_details.hand.factory import hand_factory
from unstable_unicorns_game.game_details.nursery.factory import nursery_factory
from unstable_unicorns_game.game_details.player.factory import player_factory, all_players_factory
from unstable_unicorns_game.game_details.stable.factory import stable_factory
from unstable_unicorns_game.game_details.utilities.logger import Logger
from unstable_unicorns_game.game_details.utilities.verbose_printer import VerbosePrinter
from unstable_unicorns_game.play_deciders.decider_type import DeciderType
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider

N_STARTING_CARDS = 4


def create(players: list[str], decider: PlayDecider) -> Game:
    """ Creates a game instance from the given players and decider. """
    verbose_printer = VerbosePrinter(decider.decider_type == DeciderType.CLI)
    logger = Logger(decider.decider_type == DeciderType.CLI)
    verbose_printer.print("Creating game: ")

    # TODO - allow filtering based on choice of deck.
    deck = deck_factory.create(card_factory.create_all())
    verbose_printer.print(f"\tDeck: created ({len(deck)})")
    nursery = nursery_factory.create_default()
    verbose_printer.print(f"\tNursery: created")

    # TODO -> improve this -> either create initially empty hands or use a builder (of some kind).
    cards_for_hands = [[] for _ in range(len(players))]
    for _ in range(N_STARTING_CARDS):
        for hand in cards_for_hands:
            hand.append(deck.draw_top())

    hands = [hand_factory.create(hand, decider) for hand in cards_for_hands]
    verbose_printer.print("Players: ")
    player_list = [
        player_factory.create(name, hand, stable_factory.create(nursery.get_baby()), verbose_printer)
        for name, hand in zip(players, hands)]

    game = Game(deck, discard_pile_factory.create_default(), nursery, all_players_factory.create(player_list),
                verbose_printer)

    logger.game_creation(game)
    return game
