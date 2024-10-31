""" tests for the widget class. """
from simulation.graphics.utility import Widget


class TestMakeStyleStr:

    def test_one_item(self):
        assert Widget._make_style_str({"background-color": "red"}) == "background-color: red;"

    def test_multiple_items(self):
        result = Widget._make_style_str(
            {"background-color": "red", "border-radius": "10px", "border-width": "2px"})
        assert result == "background-color: red; border-radius: 10px; border-width: 2px;"
