""" card test."""
from unstable_unicorns_game.game.card.card import Card


def test_get_descriptor_for_minimal_printing():
    card = Card.create({
        "name": "Basic Unicorn",
        "type": "basic unicorn",
        "text": "#basic #basic #basic"
    })

    expected_text = "Basic Unicorn (Basic Unicorn): #basic #basic #basic"

    assert card.get_descriptor_for_minimal_printing() == expected_text
