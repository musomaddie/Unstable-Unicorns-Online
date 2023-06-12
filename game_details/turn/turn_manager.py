class TurnManager:
    """ Manages a complete turn.

    A turn has 4 phases:
        (1) Beginning of turn: any beginning of turn actions
        (2) Draw: Draw one card from the draw pile
        (3) Action: either draw again or play a card
        (4) End: discard down to the hand limit (default 7).
    """

