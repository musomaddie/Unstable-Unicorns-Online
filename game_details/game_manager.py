import sqlite3
import os
import sys
import random

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("game_details")])
from game_details.Card import Card
from game_details.Player import Player

DB_NAME = "db/UnstableUnicorns.db"
DECK = []
DISCARD_PILE = []
PLAYERS = []
NURSERY = []
WIN_NUMBER = 7  # TODO: modify based on number of players


def _move_next_work(card, fw, args):
    """ Handles finding and moving to the next state.

    Parameters:
        card: the card that determines the next movement
        fw: the dictionary mapping functions to card names
        args: the args to be passed to the function
    """
    if card.in_dict(fw):
        return fw[card.name](args)
    return None


def _handle_beginning_turn_action(current_player):
    """ Handles the beginning of turn action.

        Parameters:
            current_player: the player whose turn it is
    """
    pass


def _handle_draw(players):
    """ Handles the draw action for the given players

        Parameters:
            players: a list of all players to draw
    """
    pass


def _handle_leave_stable(args):
    """ Handles the unicorn card leaving the given players stable

        Parameters:
            args:
                player: the player's whose stable it is
                card: the card to leave the stable

    """
    player, card = args
    player.remove_card_from_stable(card)
    # Handle leave effects
    if not card.action_on_leave:
        _move_to_discard(player, card)


def _stop_effect_triggering(args):
    """ Turns off the card effect for the given card.

        Parameters:
            args:
                unicorn: the card to turn the effect off
                played_card: the card that determines the next action
                player: the player that owns the card (if applicable)
    """
    unicorn, played_card, player = args
    unicorn.effect_will_be_triggered = False
    future_work = {
        "A Cute Attack": _handle_leave_stable
    }
    # args = (current_player, card)
    _move_next_work(played_card, future_work, [player, unicorn])


def _choose_unicorn_choice_made(choice, args):
    """ Handles the action of the chosen unicorn.

        Parameters:
            args:
                possible_cards: all the unicorns to choose from
                played_card: the card that determines the next action
                player: the player whose stable it is (if applicable)
    """
    possible_cards, played_card, player = args
    unicorn = possible_cards.pop(choice)
    future_work = {
        "A Cute Attack": _stop_effect_triggering
    }
    _move_next_work(played_card, future_work, [unicorn, played_card, player])


def _choose_unicorn(args):
    """ Handles the choosing of a unicorn.

        Parameters:
            args:
                possible_cards: all unicorns to choose from
                played_card: the card that determines the next action
                player: the player whose stable it is (if applicable)
    """
    possible_cards, played_card, player = args
    print("The possible unicorns are: ", possible_cards)
    # choice = input("Choose (number): ")
    choice = 0
    _choose_unicorn_choice_made(choice, args)


def _choose_player_choice_made(choice, args):
    """ Handles the action after the choice of a player

        Parameters:
            args:
                current_player: the player who choose the other
                card: the card played that determines the next action

        Returns:
            the chosen player
    """
    chosen_player = PLAYERS[choice]
    # Returning so A Cute Attack Can Use It
    return chosen_player


def _choose_player(args):
    """ Handles the choosing of a player.

        Parameters:
            args:
                current_player: the player to choose the other
                card: the card played that determines the next action

        Returns:
            the chosen player
    """
    current_player, card = args
    print("The players are: ", PLAYERS)
    # choice = input("Choose (number): ")
    choice = 1
    # Returning so A Cute Attack Can Use it
    return _choose_player_choice_made(choice, args)


def _add_baby_unicorn(args):
    """ Adds a baby unicorn to the given players stable

        Parameters:
            args:
                player: the player whose Stable will receive the baby unicorn

        Returns:
            True if this now meets a win condition, False otherwise
    """
    return _add_to_stable([args[0], NURSERY.pop(0)])


def _handle_a_cute_attack(args):
    """ Handles the results of the card 'A Cute Attack' being played.

        Parameters:
            args:
                current_player: the player who played the card
                card: 'A Cute Attack' card object
    """
    # TODO: to handle less unicorns!
    current_player, card = args
    chosen_player = _choose_player(args)
    for _ in range(3):
        _choose_unicorn([chosen_player.get_unicorns(), card, chosen_player])
        _add_baby_unicorn([chosen_player])


def _move_to_discard(args):
    """ Handles the movement of a given card to the discard pile.

        Parameters:
            args:
                current_player: the player whose turn it is
                card: the card to send to discard

    """
    current_player, card = args
    # Concern with dictionary is all functions requiring same length of args
    # For now, store in list
    future_work = {
        "A Cute Attack": _handle_a_cute_attack
    }
    _move_next_work(card, future_work, [current_player, card])

    # Add to discard
    card.restore_defaults()
    # TODO: actually allow the card to leave the stable if required!
    # Could leave from multiple places though
    DISCARD_PILE.append(card)


def _handle_enter_effect(args):
    """ Handles the enter effect of the given unicorn.

        Paramters:
            args:
                player: the player whose stable the unicorn entered
                unicorn: the unicorn in question
    """
    player, unicorn = args
    # Exit early if no effect
    if not unicorn.action_on_enter:
        return


def _add_to_stable(args):
    """ Handles the addition of a given card to a given stable.

        Parameters:
            args:
                player: the player's Stable in which to add the card
                unicorn: the unicorn in which to add to the Stable.

        Returns:
            True if the win condition if met, False otherwise
    """
    player, unicorn = args
    player.add_to_stable(unicorn)
    _handle_enter_effect(args)

    # TODO: maybe need some way of determining WHICH player won
    return player.has_won(WIN_NUMBER)


def _handle_card_play(current_player, card):
    """ Handles the play of a given card
    """
    if card.is_magic_type():
        return _move_to_discard([current_player, card])
    return _add_to_stable([current_player, card])


def _handle_end_turn(current_player):
    """ Handles the end turn phase of a players turn
    """
    pass


# Manages the turn: will return True if winning condition is met
def player_turn(current_player):
    print(f"It is {current_player}")

    # Beginning of Turn Action
    _handle_beginning_turn_action(current_player)

    # Draw card
    _handle_draw(current_player)

    # Action phase
    # action = input("Action? ")
    won = False
    action = 0
    if action == "draw":
        _handle_draw(current_player)
    else:  # Assuming typed card correctly (will number)
        # This handles retrieving the card from the players hand (including
        # removal)
        won = _handle_card_play(current_player,
                                current_player.play_card(action))

    # End of turn action
    _handle_end_turn(current_player)

    # Check for winning condition (look at the value of won)
    return True


def play_game():
    counter = 0
    while True:
        if player_turn(PLAYERS[counter % len(PLAYERS)]):
            break
        counter += 1


def create_game(starting_decks, player_names):
    # New game so wipe any existing data
    DECK.clear()
    DISCARD_PILE.clear()
    PLAYERS.clear()
    NURSERY.clear()
    valid_decks = ["Standard", "Rainbow", "Dragon", "Uncut", "NSFW"]

    if len(starting_decks) == 0:
        return
    if len(starting_decks) == 1 and starting_decks[0] != "Standard":
        # TODO: maybe edge case where all nonsense decks but one which isn't
        # standard
        return

    if len(player_names) <= 2:  # TODO: add in more rules for less players
        return

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for deck in starting_decks:
        if deck not in valid_decks:
            continue
        cur.execute(f"""SELECT *
                        FROM card_details JOIN pack_details USING (name)
                        WHERE deck='{deck}';
                    """)
        [DECK.append(Card(result)) for result in cur.fetchall()
            for _ in range(0, result[-2]) if result[2] != "Baby Unicorn"]
    cur.execute("""SELECT *
                    FROM card_details
                    WHERE card_type = 'Baby Unicorn'
                """)
    baby_unicorn = Card(cur.fetchone())
    random.shuffle(DECK)

    cur.close()
    conn.close()

    for i in range(25):
        NURSERY.append(baby_unicorn)  # SAME CARD FOR ALL

    for player in player_names:
        PLAYERS.append(Player(player, baby_unicorn))  # SAME CARD FOR ALL

    # Deal cards out
    for i in range(5):
        for player in PLAYERS:
            player.add_card(DECK.pop(0))


if __name__ == '__main__':
    create_game(["Standard", "Dragon", "Rainbow", "NSFW", "Uncut"],
                ["Alice", "Bob", "Charlie"])
    play_game()
