from unstable_unicorns_game.game_details.card import Card
from unstable_unicorns_game.play_deciders.discard_decider import DiscardDecider


class CliDiscardDecider(DiscardDecider):
    """ A class which decides what to play based on input from the command line interface. """

    def decide(self) -> Card | None:
        self._hand.print_basics_with_index()

        # Exit early if there's no cards.
        if len(self._hand) == 0:
            return None

        valid_numbers = self._determine_valid_discard_numbers()
        prompt = f"Choose ({'|'.join(valid_numbers)}): "
        response = input(prompt)  # Would rather not deal with an exception, so convert to int later.
        while response not in valid_numbers:
            print(f"Could not understand {response}, please try again.")
            response = input(prompt)

        return self._get_chosen_card(response)
