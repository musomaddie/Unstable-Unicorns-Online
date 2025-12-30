from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.gui.resources import color


def _determine_color_from_card_type(card_type: CardType):
    type_background_color = color.grey
    match card_type:
        case CardType.MAGIC_UNICORN:
            type_background_color = color.magic_unicorn_blue
        case CardType.BASIC_UNICORN:
            type_background_color = color.basic_unicorn_purple
        case CardType.MAGIC:
            type_background_color = color.magic_green
        case CardType.BABY_UNICORN:
            type_background_color = color.baby_unicorn_pink
        case CardType.INSTANT:
            type_background_color = color.instant_red
        case CardType.UPGRADE:
            type_background_color = color.upgrade_orange
        case CardType.DOWNGRADE:
            type_background_color = color.downgrade_yellow
    return type_background_color


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
            "background-color": color.grey,
        }, "#outline": {
            "border-style": "dashed",
            "border-radius": "5px",
            "border-width": "2px",
            "border-color": "blue"
        }}


def compact_card_pile(background_color: str = color.grey):
    return {
        "*": {
            "background-color": background_color,
        }, "#outline": {
            "border-style": "dashed",
            "border-radius": "2px",
            "border-width": "2px",
            "border-color": "black"
        }
    }


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
        "#initial": {"font-size": "20px"},
        "#turn-heading": {"font-size": "22px"},
        # "#turn-heading": {"font-size": "40px"},
        # "#cards-label": {
        #     "font-size": "30px",
        #     "border-right": "1px solid gray",
        #     "padding-right": "2px"
        # }
    }


def single_card(card_type: CardType):
    return {
        "*": {"background-color": _determine_color_from_card_type(card_type), },
        "#outline": {
            "border-style": "dashed",
            "border-radius": "5px",
            "border-width": "2px",
            "border-color": "black"
        },
    }
