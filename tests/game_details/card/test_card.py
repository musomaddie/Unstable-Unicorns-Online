from game_details.card import Card, CardType


class TestConstructor:

    def test_create_card(self):
        test_name = "Test Name"
        test_type = "magic unicorn"
        text_type = "Testing text!"

        card = Card.create_card({
            "name": test_name, "type": test_type, "text": text_type
        })

        assert card.name == test_name
        assert card.card_type == CardType.MAGIC_UNICORN
        assert card.text == text_type
