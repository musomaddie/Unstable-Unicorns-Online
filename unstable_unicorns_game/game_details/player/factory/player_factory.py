""" Player factory. """
from unstable_unicorns_game.game_details.hand import Hand
from unstable_unicorns_game.game_details.hand.factory import hand_factory
from unstable_unicorns_game.game_details.player import Player
from unstable_unicorns_game.game_details.player.impl.player_impl import PlayerImpl
from unstable_unicorns_game.game_details.stable import Stable
from unstable_unicorns_game.game_details.stable.factory import stable_factory
from unstable_unicorns_game.game_details.utilities import VerbosePrinter


def create(name: str, hand: Hand, stable: Stable, verbose_printer: VerbosePrinter = VerbosePrinter(False)) -> Player:
    """ Creates and returns a player. """
    impl = PlayerImpl(name, hand, stable, verbose_printer)
    verbose_printer.print(f"\t\t{impl.name}")
    verbose_printer.print(f"\t\t\tHand\t       : {VerbosePrinter.create_card_names_str(impl.hand)}")
    verbose_printer.print(f"\t\t\tStable\t\t   :")
    verbose_printer.print(f"\t\t\t\tUnicorns   : {VerbosePrinter.create_card_names_str(impl.stable.unicorns)}")
    verbose_printer.print(f"\t\t\t\tUpgrades   : {VerbosePrinter.create_card_names_str(impl.stable.upgrades)}")
    verbose_printer.print(f"\t\t\t\tDowngrades : {VerbosePrinter.create_card_names_str(impl.stable.downgrades)}")
    return impl


def create_default(name: str) -> Player:
    """ Creates a player with the given name and otherwise default values. """
    return create(name, hand_factory.create_default(), stable_factory.create_default())
