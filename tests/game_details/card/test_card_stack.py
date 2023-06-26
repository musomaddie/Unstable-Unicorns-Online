from game_details.card import Card, CardType, CardStack


def test_add_top(fake_card):
    card_stack = CardStack()
    size_before = len(card_stack)

    card_stack.add_top(fake_card)

    assert len(card_stack) == size_before + 1
    assert card_stack[0] == fake_card

    second_card = Card("Second added card", CardType.BASIC_UNICORN, "Text")

    card_stack.add_top(second_card)

    assert len(card_stack) == size_before + 2
    assert card_stack[0].name == "Second added card"
