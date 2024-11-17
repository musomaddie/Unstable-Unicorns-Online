from unstable_unicorns_game.game_details.game.factory import game_factory
from unstable_unicorns_game.play_deciders import decider_factory


def start_game(player_names: list[str]):
    """
    Starts a game of unstable unicorns to be run via the command line interface.
    :param player_names: a list of the names of players for this game.
    :return:
    """

    this_game = game_factory.create(player_names, decider_factory.create("cli"))
