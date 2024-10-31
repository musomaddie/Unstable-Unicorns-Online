""" Filter """
from dataclasses import dataclass

from game_details.card.action.filter_type import FilterType


@dataclass
class Filter:
    """ List of filters to be applied """
    filters: list[FilterType]
