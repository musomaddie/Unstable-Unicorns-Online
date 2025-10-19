from typing import Optional

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider


def loop_until_valid(prompt: str, accepted_responses: list[str]) -> str:
    """ Loop until the user enters a valid response. """
    response = input(prompt)
    while response not in accepted_responses:
        print(f"Could not understand {response}, please try again.")
        response = input(prompt)
    return response


class CliDecider(PlayDecider):
    """ Uses input from the command line interface to decide what to play."""

    def choose_discard(self, hand: Hand) -> Optional[Card]:
        hand.print_basics_with_index()

        # Exit early if there are no cards to discard.
        if len(hand) == 0:
            return None

        valid_numbers = hand.get_card_indices_for_display()
        prompt = f"Choose ({'|'.join(valid_numbers)}): "
        return hand.get_card_from_display_index(loop_until_valid(prompt, valid_numbers))
