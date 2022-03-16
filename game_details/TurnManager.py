class TurnManager:
    """ Manages a complete turn.
    A turn has 4 phases: 
        (1) Beginning of turn: any beginning of turn actions
        (2) Draw Phrase: draw one card from the draw pile
        (3) Action Phrase: either draw again or play a card
        (4) End of Turn: discard down to the hand limit of 7 cards

    Parameters:
        current_player (PlayerManager): the player whose turn it currently is
        all_players (PlayersManager): all the players in the game
        deck (DeckManager): the deck
        discard_pile (DiscardManager): the discard pile
        nursery (NurseryManager): the nursery.

    Methods:
        start_turn(): starts the turn from phrase one.
    """

    def __init__(self, current_player, all_players, deck, discard_pile,
            nursery):
        self.current_player = current_player
        self.all_players = all_players
        self.deck = deck
        self.discard_pile = discard_pile
        self.nursery = nursery

        # Start the turn from here
        self.start_turn()

    def start_turn(self):
        print("Turn Started")
