""" Tests for cards. """
import copy

import pytest

from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.game_details.deck.deck import Deck
from unstable_unicorns_game.game_details.game.game import Game, N_STARTING_CARDS
from unstable_unicorns_game.game_details.nursery.nursery import Nursery
from unstable_unicorns_game.play_deciders.factory import decider_factory


class TestCreate:
    """ Tests for game.create """

    @pytest.fixture
    def player_names(self):
        return ["Aelin, Chaol, Dorian"]

    @pytest.fixture
    def game(self):
        return Game.create(["Aelin", "Chaol", "Dorian"], decider_factory.create("queue"))

    def test_create_deck_fullDeckWithoutDealtCards(self, game):
        from unstable_unicorns_game.game_details.card.factory import card_factory
        expected_deck = Deck.create(card_factory.create_all())
        number_of_allocated_cards = len(game.players) * N_STARTING_CARDS

        assert len(game.deck) == len(expected_deck) - number_of_allocated_cards

    def test_create_discardPile_isEmpty(self, game):
        assert len(game.discard_pile) == 0

    def test_create_nursery_fullNurseryWithoutPlayerBabies(self, game):
        expected_nursery = Nursery.create_default()
        number_of_allocated_babies = len(game.players)

        assert len(game.nursery) == len(expected_nursery) - number_of_allocated_babies


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
