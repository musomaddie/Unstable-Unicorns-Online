from game_details.card import Card, CardType
from tests.conftest import create_card_stack_with_special_first_card


def test_draw_card(fake_card):
    special_card = Card("Special", CardType.BASIC_UNICORN, "Text")
    card_pile = create_card_stack_with_special_first_card(special_card, fake_card)
    size_before = len(card_pile)

    result_card = card_pile.draw_top()

    assert result_card == special_card
    assert len(card_pile) == size_before - 1
