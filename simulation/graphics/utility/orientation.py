""" orientation enum """
from dataclasses import dataclass
from enum import Enum

from simulation.graphics.utility import GridPosition


@dataclass
class Values:
    """ values relating to orientation """
    stable_pos: GridPosition
    hand_cards_pos: list[GridPosition]
    unicorn_cards_pos: list[GridPosition]

    name_label_colspan: int = 1
    label_colspan: int = 1
    stable_colspan: int = 1


class Orientation(Enum):
    """ Represents which way a particular class is orientated. """
    # LEFT / RIGHT axis is the is long side
    HORIZONTAL = Values(
        stable_pos=GridPosition(row=2),
        hand_cards_pos=[GridPosition(col=i, row=1) for i in range(7)],
        unicorn_cards_pos=[GridPosition(col=i, row=1) for i in range(7)],

        label_colspan=7,
        stable_colspan=7,
    )

    # UP / DOWN axis is the long side.
    VERTICAL = Values(
        stable_pos=GridPosition(col=1, row=1),
        hand_cards_pos=[GridPosition(row=(i + 2)) for i in range(7)],
        unicorn_cards_pos=[GridPosition(row=(i + 1)) for i in range(7)],

        stable_colspan=2,
        name_label_colspan=2,
    )
