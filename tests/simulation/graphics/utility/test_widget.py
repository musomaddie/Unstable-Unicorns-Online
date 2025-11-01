""" tests for the widget class. """
from unstable_unicorns_game.simulation.graphics.widget import ContainerWidget


class TestMakeStyleStr:

    def test_one_item(self):
        assert ContainerWidget._make_style_str({"background-color": "red"}) == "background-color: red;"

    def test_multiple_items(self):
        result = ContainerWidget._make_style_str(
            {"background-color": "red", "border-radius": "10px", "border-width": "2px"})
        assert result == "background-color: red; border-radius: 10px; border-width: 2px;"
