from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.play_deciders.cli_decider import CliDecider
from unstable_unicorns_game.utilities.verbose_printer import VerbosePrinter


def _welcome_message():
    print("Welcome to the command line interface for Unstable Unicorns!")
    print("Starting game .... ")
    print()


def _determine_players() -> list[str]:
    print("Please enter player details now ...")
    # TODO -> make sure that player names don't allow duplicates.
    n_players = int(input("How many players? "))
    player_names = []
    for n in range(1, n_players + 1):
        player_names.append(input(f"What's player {n}'s name? "))
    print()
    return player_names


class CliRunner:

    def __init__(self):
        self.default_players = ["Aelin", "Brannon", "Chaol", "Dorian"]
        self.player_names = []
        self.game = None

    def _use_default_setup(self) -> str:
        print(f"The default setup features 4 players: {', '.join(self.default_players)}.")
        return "y"
        # return input("Would you like to set up a game with this default? (y/n) ")

    def setup(self):
        _welcome_message()
        use_default = self._use_default_setup()
        if use_default == "y":
            print("Starting game with default settings ...")
            self.player_names = self.default_players
        else:
            print("Starting game ...")
            self.player_names = _determine_players()

        decider = CliDecider()
        verbose_printer = VerbosePrinter()
        self.game = Game.create(self.player_names, decider)

        verbose_printer.print()
        verbose_printer.game_creation(self.game)

        self.game.log_start().save_log()


if __name__ == '__main__':
    runner = CliRunner()
    runner.setup()
