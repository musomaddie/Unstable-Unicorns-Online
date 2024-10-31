""" Tests for cards. """
import copy

from unstable_unicorns_game.game_details.card import Card
from unstable_unicorns_game.game_details.game import Game


class TestTakeTurn:
    """ Tests for game.take_turn """

    def test_turn_draws_card(self, game: Game):
        """ Asserts that a card is drawn at the start of the turn. """
        starting_hand_size = len(game.players[0].hand)
        starting_deck_size = len(game.deck)

        top_deck_card = game.deck[0]

        game.take_turn()

        # + 2 because the default turn action is to draw again.
        assert len(game.players[0].hand) == starting_hand_size + 2
        assert len(game.deck) == starting_deck_size - 2
        assert game.players[0].hand[0] == top_deck_card

    def test_action_phase_draw(self, game: Game):
        """ Asserts that a card is drawn from the deck as part of the draw action phase. """
        starting_hand_size = len(game.players[0].hand)
        starting_deck_size = len(game.deck)

        second_deck_card = game.deck[1]

        game.take_turn()

        # + 2 because the default turn action is to draw again.
        assert len(game.players[0].hand) == starting_hand_size + 2
        assert len(game.deck) == starting_deck_size - 2
        assert game.players[0].hand[1] == second_deck_card

    def test_discardPhase_onlyCurrentPlayer(self, game: Game, fake_card: Card):
        """ Asserts that only the current player discards even though other players have extra cards. """
        # Add 8 cards to each player's hand.
        for player in game.players:
            [player.hand.add_card(copy.copy(fake_card)) for _ in range(8)]

        game.take_turn()

        assert len(game.players[0].hand) == 7
        assert len(game.players[1].hand) == 8
        assert len(game.players[2].hand) == 8
        assert len(game.discard_pile) == 3
