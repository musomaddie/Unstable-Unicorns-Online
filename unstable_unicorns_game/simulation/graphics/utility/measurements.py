from dataclasses import dataclass


@dataclass
class Size:
    width: int
    height: int


# Prefer width 70, height 113 for golden rectangle, but manually setting to look alright on mac.
CARD_SIZE = Size(width=72, height=104)
SMALL_CARD_SIZE = Size(width=36, height=52)
