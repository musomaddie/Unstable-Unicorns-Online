""" Tests for cards. """
import pytest

from unstable_unicorns_game.game_details.card.factory import card_factory
from unstable_unicorns_game.game_details.deck import Deck
from unstable_unicorns_game.game_details.game.factory import N_STARTING_CARDS
from unstable_unicorns_game.game_details.game.factory import game_factory
from unstable_unicorns_game.game_details.nursery.factory import nursery_factory
from unstable_unicorns_game.play_deciders import DeciderType, DeciderFactory


class TestCreateGame:

    @pytest.fixture
    def player_names(self):
        """ Returns 3 player names. """
        return ["Alice", "Bob", "Charlie"]

    def test_deck_fullDeckWithoutDealtCards(self, player_names):
        expected_deck = Deck(card_factory.create_all())
        number_allocated_cards = 3 * N_STARTING_CARDS  # number of player multiplied by

        game = game_factory.create(player_names, DeciderFactory(DeciderType.QUEUE))

        assert len(game.deck) == len(expected_deck) - number_allocated_cards

    def test_discardPile_isEmpty(self, player_names):
        game = game_factory.create(player_names, DeciderFactory(DeciderType.QUEUE))

        assert len(game.discard_pile) == 0

    def test_nursery_fullNurseryWithoutPlayerBabies(self, player_names):
        expected_nursery = nursery_factory.create_default()
        number_allocated_babies = len(player_names)

        game = game_factory.create(player_names, DeciderFactory(DeciderType.QUEUE))

        assert len(game.nursery) == len(expected_nursery) - number_allocated_babies

    def test_players_playerNamesSameOrder(self, player_names):
        game = game_factory.create(player_names, DeciderFactory(DeciderType.QUEUE))
        assert game.players[0].name == player_names[0]
        assert game.players[1].name == player_names[1]
        assert game.players[2].name == player_names[2]

    # TODO - I need to patch / monkeypatch (?) the method call to create the deck.
    def test_playersHands_dealtOrder(self, player_names):
        pass
