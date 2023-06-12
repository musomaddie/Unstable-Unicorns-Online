import copy

from game_details.card import CardPile, Card, CardType


def test_draw_card(fake_card):
    card_pile = CardPile()
    special_card = Card("Special", CardType.BASIC_UNICORN, "Text")
    card_pile.cards.append(special_card)
    for _ in range(10):
        card_pile.cards.append(copy.copy(fake_card))
    size_before = len(card_pile)

    result_card = card_pile.draw_top()

    assert result_card.name == special_card.name
    assert len(card_pile) == size_before - 1
