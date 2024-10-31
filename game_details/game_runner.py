
    @staticmethod
    def create_game_with_default_deck(players: list[str]):
        """ creates a game using the default deck. """
        return Game.create_game(players, Deck(Card.create_all_cards()), Nursery.create_default())
