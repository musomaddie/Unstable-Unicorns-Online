from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.play_deciders.cli_decider import CliDecider


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
        self.game = Game.create(self.player_names, decider)

        self.game.log_start().save_log()
        print()
        print(self.game.debug_str())

    def play_game(self):
        print("Starting game ...")
        self.game.take_turn()
        # TODO -> structure this a bit better -> but for now just shove all the print statements in here.


if __name__ == '__main__':
    runner = CliRunner()
    runner.setup()
    runner.play_game()
