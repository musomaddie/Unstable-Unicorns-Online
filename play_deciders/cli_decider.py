from game_details.card import Card
from play_deciders.play_decider import PlayDecider


class CliDecider(PlayDecider):
    """ A class which decides what to play based on input from the command line interface. """

    def decide_discard(self) -> Card | None:
        hand = self.player.hand
        hand.print_basics_with_index()

        # Exit early if there's no cards.
        if len(hand) == 0:
            return None

        valid_numbers = [str(i + 1) for i in range(len(hand))]
        prompt = f"Choose ({'|'.join(valid_numbers)}): "
        response = input(prompt)  # Would rather not deal with an exception, so convert to int later.
        while response not in valid_numbers:
            print(f"Could not understand {response}, please try again.")
            response = input(prompt)

        return hand[int(response) - 1]
