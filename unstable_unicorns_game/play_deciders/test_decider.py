from unstable_unicorns_game.game_details.card import Card
from unstable_unicorns_game.play_deciders.play_decider import DiscardDecider


class TestDiscardDecider(DiscardDecider):
    """ A play decider for use in TESTS ONLY which makes decisions in the order passed. """

    def __init__(self, decisions: list[str]):
        self.decisions = decisions

    def decide_discard(self) -> Card | None:
        # Exit early if there's no cards.
        if len(self.hand) == 0:
            return None

        response = self.decisions.pop(0)
        while response not in self._determine_valid_discard_numbers():
            # Skipping the print statement as that's a little annoying in tests.
            response = self.decisions.pop(0)

        return self._get_chosen_card(response)
