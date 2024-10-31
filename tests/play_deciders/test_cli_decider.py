""" tests for the CLI decider. """
from io import StringIO

import pytest

from unstable_unicorns_game.game_details.card import CardType
from unstable_unicorns_game.game_details.card.factory import card_factory
from unstable_unicorns_game.game_details.hand import Hand
from unstable_unicorns_game.game_details.hand.factory import hand_factory
from unstable_unicorns_game.game_details.player.factory import player_factory
from unstable_unicorns_game.game_details.stable.factory import stable_factory
from unstable_unicorns_game.play_deciders.cli_decider import CliDiscardDecider


@pytest.fixture
def default_player():
    """ creates a default player for this. """
    return player_factory.create_default("Test Player")


@pytest.fixture
def hand_with_cards() -> Hand:
    """ A hand populated with multiple cards. """
    return hand_factory.create_only_cards([
        card_factory.create_default("Unicorn", CardType.BASIC_UNICORN),
        card_factory.create_default("Second unicorn", CardType.MAGIC_UNICORN)])


class TestDecideDiscard:

    def test_no_cards_no_output(self, default_player, capsys):
        decider = CliDiscardDecider(default_player.hand)
        result = decider.decide_discard()

        assert result is None
        assert len(default_player.hand) == 0
        assert capsys.readouterr().out == "You have no cards.\n"

    def test_with_one_card(self, monkeypatch, capsys):
        card = card_factory.create_default("Only card", CardType.BASIC_UNICORN)
        hand = hand_factory.create_only_cards([card])
        decider = CliDiscardDecider(hand)
        monkeypatch.setattr("sys.stdin", StringIO("1"))

        result = decider.decide_discard()

        assert result == card
        expected_lines = [
            "[1]\tOnly card (Basic Unicorn): default text",
            "Choose (1): "
        ]
        assert capsys.readouterr().out == "\n".join(expected_lines)

    def test_cards_with_failed_attempts(self, hand_with_cards, monkeypatch, capsys):
        player = player_factory.create(
            "Test player", hand_with_cards, stable_factory.create_default())
        decider = CliDiscardDecider(player.hand)

        monkeypatch.setattr("sys.stdin", StringIO("-1\noops\n2"))

        result = decider.decide_discard()

        assert result.name == "Second unicorn"
        expected_lines = [
            "[1]\tUnicorn (Basic Unicorn): default text",
            "[2]\tSecond unicorn (Magic Unicorn): default text",
            "Choose (1|2): Could not understand -1, please try again.",
            "Choose (1|2): Could not understand oops, please try again.",
            "Choose (1|2): "
        ]
        assert capsys.readouterr().out == "\n".join(expected_lines)
