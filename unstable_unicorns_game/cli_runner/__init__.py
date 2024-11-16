""" Runs the unstable unicorns game using the CLI runner. """

default_players = ["Aelin", "Brannon", "Chaol", "Dorian"]


def welcome_message():
    print("Welcome to the command line interface for Unstable Unicorns!")
    print("Starting game .... ")
    print()


def default_setup() -> str:
    print(f"The default setup features 4 players: {', '.join(default_players)}.")
    return input("Would you like to set up a game with this default? (y/n) ")


def determine_players() -> list[str]:
    print("Please enter player details now ...")
    n_players = int(input("How many players? "))
    player_names = []
    for n in range(1, n_players + 1):
        player_names.append(input(f"What's player {n}'s name? "))
    print()
    return player_names


def run():
    welcome_message()
    use_default = default_setup()
    player_names = []
    if use_default == "y":
        print("Starting game with default settings ...")
        player_names = default_players
        print()
    else:
        print()
        player_names = determine_players()


if __name__ == '__main__':
    run()
