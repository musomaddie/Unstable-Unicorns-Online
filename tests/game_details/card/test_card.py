""" card test."""
from game_details.card.factory import card_factory


def test_get_descriptor_for_minimal_printing():
    card = card_factory.create({
        "name": "Basic Unicorn",
        "type": "basic unicorn",
        "text": "#basic #basic #basic"
    })

    expected_text = "Basic Unicorn (Basic Unicorn): #basic #basic #basic"

    assert card.get_descriptor_for_minimal_printing() == expected_text
