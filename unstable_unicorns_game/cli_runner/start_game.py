from unstable_unicorns_game.game_details.game.factory import game_factory
from unstable_unicorns_game.play_deciders.factory import decider_factory


def start_game(player_names: list[str]):
    """
    Starts a game of unstable unicorns to be run via the command line interface.
    :param player_names: a list of the names of players for this game.
    :return:
    """

    this_game = game_factory.create(player_names, decider_factory.create("cli"))

    # TODO -> format printing a bit better? set a max column width?
    # Can print in this file directly without verbose print since the verbose_printer will always print
    print("")
    print("=" * 160)
    print()

    # TODO -> centralize this between runners (somehow ... )
    turn_number = 1
    while True:
        print(f"Taking turn #{turn_number}", end=' ')
        this_game.take_turn()

        break
