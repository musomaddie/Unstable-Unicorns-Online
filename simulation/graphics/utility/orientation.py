""" orientation enum """
from dataclasses import dataclass
from enum import Enum

from simulation.graphics.utility import GridPosition


@dataclass
class Values:
    """ values relating to orientation """
    label_colspan: int
    stable_colspan: int
    stable_pos: GridPosition
    hand_card_pos: list[GridPosition]


class Orientation(Enum):
    """ Represents which way a particular class is orientated. """
    # UP / DOWN axis is the long side.
    VERTICAL = Values(
        label_colspan=1,
        stable_colspan=2,
        stable_pos=GridPosition(col=1, row=1),
        hand_card_pos=[GridPosition(col=0, row=(i + 1)) for i in range(7)],
    )

    # LEFT / RIGHT axis is the  is long side
    HORIZONTAL = Values(
        label_colspan=7,
        stable_colspan=7,
        stable_pos=GridPosition(col=0, row=2),
        hand_card_pos=[GridPosition(col=i, row=1) for i in range(7)],
    )
