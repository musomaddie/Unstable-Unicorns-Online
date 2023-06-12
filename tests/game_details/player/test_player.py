from game_details.card import Card, CardType
from game_details.player import Player
from tests.conftest import create_card_stack_with_special_first_card


def test_draw_card(fake_card):
    testing_card = Card("Testing First", CardType.BASIC_UNICORN, "Text")
    player = Player("Alice")
    deck = create_card_stack_with_special_first_card(testing_card, fake_card)
    deck_size_before = len(deck)
    hand_size_before = len(player.hand)

    player.draw_card(deck)

    assert len(deck) == deck_size_before - 1
    assert len(player.hand) == hand_size_before + 1
    assert testing_card in player.hand
