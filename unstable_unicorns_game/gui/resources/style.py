from unstable_unicorns_game.gui.resources.color import grey


def testing_border():
    return {
        "*": {
            "border": "1px solid black",
        }}


def table_center_pile_wrapper():
    return {
        "*": {
            "font-size": "16px",
        }, "#container": {
            "border-style": "solid",
            "border-width": "3",
            "border-color": "navy",
            "border-radius": "20",
        }}


def card_piles():
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


def button():
    return {
        "font-size": "14px"
    }


def player_space(color_code: str):
    return {
        "*": {
            "background-color": color_code,
            # "font-family": "Itim",
        },
        "#name": {
            #     # "font-family": "Manhattan Darling",
            "font-size": "20px"
        },
        # "#initial": {"font-size": "26px"},
        # "#turn-heading": {"font-size": "40px"},
        # "#cards-label": {
        #     "font-size": "30px",
        #     "border-right": "1px solid gray",
        #     "padding-right": "2px"
        # }
    }
