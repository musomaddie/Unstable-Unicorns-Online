""" card factory. """
import json

from unstable_unicorns_game.game_details.card.card import Card


# TODO -> move this to live somewhere else! (maybe in game ??)
def create_all() -> list['Card']:
    """ Creates card objects for every card within the json file. """
    file_contents = json.load(open("unstable_unicorns_game/data/card_details.json"))
    # TODO - temporary for testing, delete this later!!
    cards = [Card.create(card_info) for card_info in file_contents]
    while len(cards) < 30:
        cards.append(cards[0])
    return cards
