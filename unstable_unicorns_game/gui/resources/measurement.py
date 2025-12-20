from dataclasses import dataclass
from typing import Optional


@dataclass
class Size:
    width: int
    height: int


@dataclass
class Margins:
    top: Optional[int] = None
    bottom: Optional[int] = None
    left: Optional[int] = None
    right: Optional[int] = None


# Prefer width 70, height 113 for golden rectangle, but manually setting to look alright on mac.
# This was a previous card size, but I'm sizing things down a little now.
CARD_SIZE = Size(width=72, height=104)
SMALL_CARD_SIZE = Size(width=36, height=52)

CENTER_CARD_PILE_SPACING = 20
CENTER_CARD_PILE_MARGINS = Margins(10, 10, 10, 10)
