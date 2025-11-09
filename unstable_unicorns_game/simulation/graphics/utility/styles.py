from unstable_unicorns_game.simulation.graphics.utility.colours import grey

# Prefer width 70, height 113 for golden rectangle, but manually setting to look alright on mac.
CARD_WIDTH = 72
CARD_HEIGHT = 104
SMALL_CARD_WIDTH = 36
SMALL_CARD_HEIGHT = 52


def compact_card_pile_player(color: str = grey):
    return {
        "*": {
            "background-color": color,
            "font-size": "20px",
        },
        "#container": {
            "border-style": "dashed",
            "border-radius": "2px",
            "border-width": "2px",
            "border-color": "black"
        }}


def player_ui_labels(compact: bool = False):
    if compact:
        return {"#compact-lbl": {
            "font-size": "20px",
        }}

    return {"#lbl": {
        # "font-family": "Permanent Marker",
        "font-size": "20px",
        "border-right": "1px solid gray",
        "padding-right": "2px",
        "color": "gray"
    }}


def table_center_card_piles_wrapper():
    return {"#container": {
        "border-style": "solid",
        "border-width": "3",
        "border-color": "navy",
        "border-radius": "20",
    }}


def table_center_card_piles():
    return {
        "*": {
            "background-color": grey,
        },
        "#outline": {
            "border-style": "dashed",
            "border-radius": "5px",
            "border-width": "2px",
            "border-color": "blue"
        }}


def single_card():
    return {
        "*": {
            "background-color": grey,
        },
        "#outline": {
            "border-style": "dashed",
            "border-radius": "5px",
            "border-width": "2px",
            "border-color": "black"
        }}


def player_board(color_code: str):
    return {
        "*": {
            "background-color": color_code,
            # "font-family": "Itim",
        },
        "#name": {
            # "font-family": "Manhattan Darling",
            "font-size": "50px"
        },
        "#initial": {"font-size": "26px"},
        "#turn-heading": {"font-size": "40px"},
        "#cards-label": {
            "font-size": "30px",
            "border-right": "1px solid gray",
            "padding-right": "2px"
        }
    }
