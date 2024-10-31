""" card factory tests. """
from unstable_unicorns_game.game_details.card import CardType
from unstable_unicorns_game.game_details.card.factory import card_factory


# noinspection PyClassHasNoInit
class TestConstructor:

    def test_create_card_without_effect(self):
        test_name = "Test Name"
        test_type = "magic unicorn"
        text_type = "Testing text!"

        card = card_factory.create({
            "name": test_name, "type": test_type, "text": text_type
        })

        assert card.name == test_name
        assert card.card_type == CardType.MAGIC_UNICORN
        assert card.text == text_type

    def test_create_card_with_effect(self):
        # TODO test here.
        pass
