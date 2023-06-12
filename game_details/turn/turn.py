from dataclasses import dataclass

from game_details.deck.deck_manager import DeckManager
from game_details.discard_pile.discard_pile_manager import DiscardPileManager
from game_details.nursery import NurseryManager
from game_details.player import PlayerManager, AllPlayersManager


@dataclass
class Turn:
    """ A dataclass for all turn related objects. """
    deck_manager: DeckManager
    discard_pile_manager: DiscardPileManager
    nursery_manager: NurseryManager
    current_player_manager: PlayerManager
    all_players_manager: AllPlayersManager
