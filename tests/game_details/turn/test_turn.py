import copy
from io import StringIO
from unittest.mock import MagicMock, call

import pytest

from game_details.card import Card, CardType
from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.nursery import Nursery
from game_details.player import Player, AllPlayers
from game_details.turn import Turn


@pytest.fixture
def fake_card():
    return Card("Name", CardType.BASIC_UNICORN, "Text")


class TestTakeTurnSteps:
    @pytest.fixture
    def deck(self, fake_card) -> Deck:
        return Deck([copy.copy(fake_card) for _ in range(5)])

    @pytest.fixture
    def discard_pile(self) -> DiscardPile:
        return DiscardPile()

    @pytest.fixture
    def nursery(self) -> Nursery:
        return Nursery()

    @pytest.fixture
    def players(self) -> list[Player]:
        return [Player("Alice"), Player("Bob"), Player("Charlie")]

    @pytest.fixture
    def turn(self, deck, discard_pile, nursery, players):
        return Turn(deck, discard_pile, nursery, players[0], AllPlayers(players))

    def test_draws_card(self, turn, players, deck):
        starting_hand_size = len(players[0].hand)
        starting_deck_size = len(deck)
        # TODO - use monkeypatch method to remove the first draw from this test.
        top_deck_card = deck[0]

        turn.take_turn()
        # The default action phase is to draw again so should be starting_hand_size + 2
        assert len(players[0].hand) == starting_hand_size + 2
        assert len(deck) == starting_deck_size - 2
        assert top_deck_card == players[0].hand[0]

    def test_beginning_of_turn_action(self, deck, discard_pile, nursery):
        # Use some fake players instead of actual to verify the beginning of turn action.
        players = [MagicMock(), MagicMock(), MagicMock()]
        turn = Turn(deck, discard_pile, nursery, players[0], AllPlayers(players))

        turn.take_turn()

        assert call.take_beginning_of_turn_action() in players[0].mock_calls

    def test_action_phase_draw(self, deck, players, turn):
        starting_hand_size = len(players[0].hand)
        starting_deck_size = len(deck)
        second_draw_card = deck[2]

        turn.take_turn()

        assert len(players[0].hand) == starting_hand_size + 2
        assert len(deck) == starting_deck_size - 2
        assert players[0].hand[1] == second_draw_card

    def test_discard_phase_not_required(self, players, turn):
        starting_hand_size = len(players[0].hand)
        turn.take_turn()

        # Default turn action is to draw, so we expect +2 cards.
        assert len(players[0].hand) == starting_hand_size + 2

    def test_discard_phase_only_starting_player(self, players, turn, discard_pile, fake_card, monkeypatch):
        # Add 8 cards to each players hand.
        for player in players:
            [player.hand.add_card(copy.copy(fake_card)) for _ in range(8)]
        # Just keep discarding the first card in the hand
        monkeypatch.setattr("sys.stdin", StringIO("1\n1\n1"))

        turn.take_turn()

        # The first players hand size should be the hand limit - 7
        assert len(players[0].hand) == 7
        # Remaining players hand size should be unchanged.
        assert len(players[1].hand) == 8
        assert len(players[2].hand) == 8
        # Should have 3 cards in the discard pile.
        assert len(discard_pile) == 3
