from _pytest.fixtures import fixture

from game_details.card import Card
from game_details.deck import Deck
from game_details.game_runner import Game, N_STARTING_CARDS
from game_details.nursery import Nursery


class TestCreateGame:

    @fixture
    def player_names(self):
        return ["Alice", "Bob", "Charlie"]

    def test_deck_fullDeckWithoutDealtCards(self, player_names):
        expected_deck = Deck(Card.create_all_cards())
        number_allocated_cards = 3 * N_STARTING_CARDS  # number of player multiplied by

        game = Game.create_game(player_names)

        assert len(game.deck) == len(expected_deck) - number_allocated_cards

    def test_discardPile_isEmpty(self, player_names):
        game = Game.create_game(player_names)

        assert len(game.discard_pile) == 0

    def test_nursery_fullNurseryWithoutPlayerBabies(self, player_names):
        expected_nursery = Nursery()
        number_allocated_babies = len(player_names)

        game = Game.create_game(player_names)

        assert len(game.nursery) == len(expected_nursery) - number_allocated_babies

    def test_players_playerNamesSameOrder(self, player_names):
        game = Game.create_game(player_names)
        assert game.players[0].name == player_names[0]
        assert game.players[1].name == player_names[1]
        assert game.players[2].name == player_names[2]

    # TODO - I need to patch / monkeypatch (?) the method call to create the deck.
    def test_playersHands_dealtOrder(self, player_names):
        pass
