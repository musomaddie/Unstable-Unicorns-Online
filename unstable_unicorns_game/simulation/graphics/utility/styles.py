from unstable_unicorns_game.simulation.graphics.utility.colours import GREY

# Prefer width 70, height 113 for golden rectangle, but manually setting to look alright on mac.
CARD_WIDTH = 72
CARD_HEIGHT = 104
SMALL_CARD_WIDTH = 36
SMALL_CARD_HEIGHT = 52

compact_card_pile_for_player_hand = {
    "*": {
        "background-color": GREY,
        "font-size": "20px",
    },
    "#container": {
        "border-style": "dashed",
        "border-radius": "2px",
        "border-width": "2px",
        "border-color": "black"
    }}

player_ui_labels = {
    "#lbl": {
        # "font-family": "Permanent Marker",
        "font-size": "20px",
        "border-right": "1px solid gray",
        "padding-right": "2px",
        "color": "gray"
    }}

table_center_card_piles_wrapper = {
    "#container": {
        "border-style": "solid",
        "border-width": "3",
        "border-color": "navy",
        "border-radius": "20",
    }}

table_center_card_piles = {
    "*": {
        "background-color": GREY,
    },
    "#outline": {
        "border-style": "dashed",
        "border-radius": "5px",
        "border-width": "2px",
        "border-color": "blue"
    }}

single_card = {
    "*": {
        "background-color": GREY,
    },
    "#outline": {
        "border-style": "dashed",
        "border-radius": "5px",
        "border-width": "2px",
        "border-color": "black"
    }}
