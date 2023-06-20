import copy
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
    def deck(self) -> Deck:
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
