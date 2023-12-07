from game_details.card import Card
from play_deciders.play_decider import DiscardDecider


class CliDiscardDecider(DiscardDecider):
    """ A class which decides what to play based on input from the command line interface. """

    def decide_discard(self) -> Card | None:
        self.hand.print_basics_with_index()

        # Exit early if there's no cards.
        if len(self.hand) == 0:
            return None

        valid_numbers = [str(i + 1) for i in range(len(self.hand))]
        prompt = f"Choose ({'|'.join(valid_numbers)}): "
        response = input(prompt)  # Would rather not deal with an exception, so convert to int later.
        while response not in valid_numbers:
            print(f"Could not understand {response}, please try again.")
            response = input(prompt)

        return self.hand[int(response) - 1]
