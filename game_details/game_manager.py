import sqlite3
import os
import sys
import random
import copy

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("game_details")])
from game_details.Card import Card
from game_details.Player import Player
from game_details.CardLocation import CardLocation

DB_NAME = "db/UnstableUnicorns.db"
DECK = []
DISCARD_PILE = []
PLAYERS = []
NURSERY = []
WIN_NUMBER = 7  # TODO: modify based on number of players


def _move_next_state(card, fw, args):
    """ Handles finding and moving to the next state.

    Parameters:
        card: the card that determines the next movement
        fw: the dictionary mapping functions to card names
        args: the args to be passed to the function
    """
    if not card:
        return False
    if card.in_dict(fw):
        return fw[card.name](args)
    return False


def _add_baby_unicorn(args):
    """ Adds a baby unicorn to the given players stable

        Parameters:
            args:
                player: the player whose Stable will receive the baby unicorn

        Returns:
            True if this now meets a win condition, False otherwise
    """
    return _add_to_stable([args[0], NURSERY.pop(0), None])


def _add_to_hand(args):
    """ Adds a card to the players hand

        Parameters:
            args:
                player: the player to add to the Hand over
                card: the card to add to the hand
    """
    player, card = args
    card.location = CardLocation.HAND
    player.add_to_hand(card)


def _add_to_stable(args):
    """ Handles the addition of a given card to a given stable.

        Parameters:
            args:
                player: the player's Stable in which to add the card
                card: the unicorn to be added
                played_card: the played_card (if needed)

        Returns:
            True if the win condition if met, False otherwise
    """
    player, card, played_card = args
    player.add_to_stable(card)
    card.location = CardLocation.STABLE

    if player.barbed_wire_effect:
        _handle_discard_card([player, None, None])

    _handle_enter_effect([player, card])

    # TODO: maybe need some way of determining WHICH player won
    return player.has_won(WIN_NUMBER)


def _apply_person_effect(args):
    """ Applies or removes the effect corresponding to the given card for the
    given player.

        Parameters:
            args:
                player: the player on which to apply the effect
                card: the card to determine the effect
    """
    player, card = args
    if card == "Barbed Wire":
        player.barbed_wire_effect = not player.barbed_wire_effect
    elif card == "Black Knight Unicorn":
        player.unicorn_destroy_decoy = not player.unicorn_destroy_decoy
    elif card == "Blinding Light":
        player.unicorn_effects_blocked = not player.unicorn_effects_blocked
    elif card == "Blow Up Unicorn":
        player.unicorn_destroy_decoy = not player.unicorn_destroy_decoy
        player.unicorn_sacrifice_decoy = not player.unicorn_sacrifice_decoy
    elif card == "Cupcakes For Everyone":
        player.share_upgrades = not player.share_upgrades


def _apply_to_everyone(args):
    """ Does the corresponding action for every Player

        Parameters:
            args:
                current_player: the player who played the initial card
                card: the card that has been played
    """
    current_player, card = args
    future_work = {
        "Angry Dragoncorn": _handle_discard_card,
        "Cotton Candy Llamacorn": _handle_choose_card_sacrifice,
        "Cult Leader Unicorn": _handle_choose_card_sacrifice,

    }
    for player in PLAYERS:
        _move_next_state(card, future_work, [player, card, None])


def _check_proceed_with_action(args):
    """ Confirms if the user wants to proceed with action
    and proceed with action if so

        Parameters:
            args:
                player: the player playing the card
                card: the card in question.
                trash: additional value NOT required, but included
                    for consistency

        Returns:
            TRUE if win condition met, otherwise FALSE

    """
    player, card, trash = args
    # proceed = input(f"Proceed with action for ${card}? ")
    proceed = "yes"
    if proceed.lower() != "yes":
        return False

    future_work = {
        "Angel Unicorn": _handle_sacrifice_this_card,
        "Black Knight Unicorn": _handle_sacrifice_this_card,
        "Blow Up Unicorn": _handle_sacrifice_this_card,
    }
    return _move_next_state(card, future_work, [player, card, None])


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
    # choice = input("Choose (number): ")
    # print("The players are: ", PLAYERS)
    choice = 1
    # Returning so A Cute Attack Can Use it  TODO: change this to be consistent
    # with other state management
    return _choose_player_choice_made(choice, args)


def _choose_player_choice_made(choice, args):
    """ Handles the action after the choice of a player

        Parameters:
            args:
                current_player: the player who chooses the other
                card: the card played that determines the next action

        Returns:
            the chosen player
    """
    cur_player, card = args
    chosen_player = PLAYERS[choice]
    # Returning so A Cute Attack Can Use It
    future_states = {
        "Annoying Flying Unicorn": _handle_discard_card,
        "Back Kick": _handle_return_to_hand,
        "Blatant Thievery": _handle_look_at_hand,
    }
    # TODO: not sure if best way to structure this
    if card.card_type != "Magic" and not card.is_unicorn():
        _add_to_stable([chosen_player, card, card])
    else:
        _move_next_state(card, future_states,
                         [chosen_player, card, cur_player])
    return chosen_player


def _choose_unicorn(args):
    """ Handles the choosing of a unicorn.

        Parameters:
            args:
                player: the player whose stable it is (if applicable)
                played_card: the card that determines the next action
                possible_cards: all unicorns to choose from
    """
    player, played_card, possible_cards = args
    # choice = input("Choose (number): ")
    choice = 0
    _choose_unicorn_choice_made(choice, args)


def _choose_unicorn_choice_made(choice, args):
    """ Handles the action of the chosen unicorn.

        Parameters:
            args:
                player: the player whose stable it is (if applicable)
                played_card: the card that determines the next action
                possible_cards: all the unicorns to choose from

        Returns:
            TRUE if win condition met otherwise FALSE
    """
    player, played_card, possible_cards = args
    unicorn = possible_cards[choice]
    future_work = {
        "A Cute Attack": _remove_unicorn_stop_effect_triggering,
        "Angel Unicorn": _handle_leave_discard,
    }
    return _move_next_state(played_card, future_work,
                            [player, unicorn, played_card])


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
        _choose_unicorn([chosen_player, card, chosen_player.get_unicorns()])
        _add_baby_unicorn([chosen_player])


def _handle_beginning_turn_action(current_player):
    """ Handles the beginning of turn action.

        Parameters:
            current_player: the player whose turn it is

        Returns:
            TRUE if win condition met, otherwise FALSE
    """
    future_work = {
        "Angel Unicorn": _check_proceed_with_action,
        "Autoerotic Asphyxiation": _handle_discard_card
    }
    # go through each card and check
    result = False
    for card in current_player.stable:
        if not card.action_on_start:
            continue
        # Check if the activation is blocked and skip
        if card.is_unicorn() and current_player.unicorn_effects_blocked:
            continue

        result = _move_next_state(card, future_work,
                                  [current_player, card, None])
        # Quit early if the player has won!
        if result:
            return result

    return result


def _handle_card_play(current_player, card):
    """ Handles the play of a given card for the given player

        Parameters:
            current_player: the player playing the card
            card: the card being played
    """

    if card.is_magic_type():
        return _move_to_discard([current_player, card])
    if card.is_unicorn():
        return _add_to_stable([current_player, card, card])
    # Remaining are upgrades and downgrades: need to choose the stable
    return _choose_player([current_player, card])


def _handle_check_unicorns_and_apply_states(args):
    """ Activates when a state blocking card has left. Applies any applicable
    states.

        Parameters:
            args:
                player: the player whose stable needs to be checked
                played_card: the card that has left the stable

    """
    player, played_card = args
    future_states = {
        "Black Knight Unicorn": _apply_person_effect,
    }
    for card in player.stable:
        _move_next_state(card, future_states, [player, card])


def _handle_choose_card_destroy(args):
    """ Handles choosing a card to destroy.

        Parameters:
            args:
                player: the player choosing which card to destroy.
                card: the card to determine the next move
    """
    player, card = args
    chosen_player = _choose_player(args)
    possible_cards = chosen_player.stable
    # Is the possible cards different to just the stable?
    if card == "Chainsaw Unicorn":
        possible_cards = chosen_player._get_stable_modifiers()

    if len(possible_cards) == 0:
        return player.has_won(WIN_NUMBER)

    # print(possible_cards)
    # choice = int(input("Card? "))
    choice = 1

    chosen_card = possible_cards[choice]

    return _handle_destroy([player, chosen_card, card])


def _handle_choose_card_sacrifice(args):
    """ Handles choosing a card to sacrifice.

        Parameters:
            args:
                player: the player who is choosing a card to sacrifice
                card: the card played that determines any constraints or
                    future states.
                trash: only needed for consistency

    """
    player, card, trash = args
    possible_cards = player.stable
    # Is possible cards different to complete stable?
    if card == "Chainsaw Unicorn":
        possible_cards = player.get_stable_modifiers()
    elif card == "Cotton Candy Llamacorn" or card == "Cult Leader Unicorn":
        possible_cards = player.get_unicorns()

    # Return early if nothing to choose
    if len(possible_cards) == 0:
        return player.has_won(WIN_NUMBER)

    # Make choice and return
    # print(possible_cards)
    # choice = int(input("Card? "))
    choice = 0
    chosen_card = possible_cards[choice]

    return _handle_sacrifice_this_card([player, chosen_card, card])


def _handle_destroy(args):
    """ Handles the destroying of a given card.

    TODO: will need some way of determining which player this should be shown
    to.

        Parameters:
            args:
                player: the player whose card is being destroyed
                card: the card to be destroyed
                played_card: the card to determine next move (if applicable)

        Returns:
        True if the win condition has been met, False otherwise
    """
    player, card, played_card = args

    # Check if there is something preventing this
    if player.unicorn_destroy_decoy:
        card = player.sacrifice_instead()
        if not (card.is_unicorn and player.unicorn_effects_blocked):
            _check_proceed_with_action([player, card])

    # Check it hasn't already been discarded
    if card.location == CardLocation.DISCARD_PILE:
        return

    _handle_leave_stable([player, card, None])

    # Check for returning to hand
    if card.return_to_hand:
        _add_to_hand([player, card])
        return player.has_won()

    DISCARD_PILE.append(card)
    return player.has_won


def _handle_discard_card(args):
    """ Handles the given player discarding a card.

        Parameters:
            args:
                player: the player to discard a card
                played_card: the card that has been played
                trash: additional value not required but passed for consistency

    """
    player, played_card, trash = args
    # print(f"Your hand contains: {player.hand}")
    # choice = int(input("Card: "))
    choice = 1
    _handle_discard_card_choice_made(choice, args)


def _handle_discard_card_choice_made(choice, args):
    """ Handles moving the given card from a players hand to the discard pile

        Parameters:
            choice: the index of the chosen card
            args:
                player: the player who is discard the card
    """
    # Remove the given card from the players hand
    player = args[0]
    card = player.hand.pop(choice)
    _move_to_discard([player, card])


def _handle_draw(args):
    """ Handles the draw action for the given players

        Parameters:
            args:
                player: the player to draw
                card: the card determining the next action
                trash: required for consistency
    """
    player, card, trash = args
    card = DECK.pop(0)
    player.add_to_hand(card)


def _handle_end_turn(current_player):
    """ Handles the end turn phase of a players turn
    """
    pass


def _handle_enter_effect(args):
    """ Handles the enter effect of the given unicorn.

        Paramters:
            args:
                player: the player whose stable the unicorn entered
                card: the card in question
    """

    player, card = args

    future_work = {
        "Angry Dragoncorn": _apply_to_everyone,
        "Annoying Flying Unicorn": _choose_player,
        "Barbed Wire": _apply_person_effect,
        "Bear Daddy Unicorn": _handle_search_deck,
        "Black Knight Unicorn": _apply_person_effect,
        "Blinding Light": _apply_person_effect,
        "Blow Up Unicorn": _apply_person_effect,
        "Chainsaw Unicorn": _handle_sacrifice_or_destroy,
        "Classy Narwhal": _handle_search_deck,
        "Cotton Candy Llamacorn": _apply_to_everyone,
        "Cult Leader Unicorn": _apply_to_everyone,
        "Cupcakes For Everyone": _handle_share_upgrades,
    }
    if card.is_unicorn() and player.unicorn_effects_blocked:
        return
    _move_next_state(card, future_work, args)

    # Share the upgrade if required
    if player.share_upgrades and card.is_upgrade():
        _handle_share_this_upgrade([player, card])


def _handle_leave_discard(args):
    """ Handles the given card leaving the discard pile

        Parameters:
            args:
                player: the player whose stable is effected
                card: the card leaving the discard pile
                played_card: the card to trigger this, and determine next state
    """
    player, card, played_card = args
    _remove_card_from_discard(card)
    future_work = {
        "Angel Unicorn": _add_to_stable
    }
    _move_next_state(played_card, future_work, args)


def _handle_leave_stable(args):
    """ Handles the unicorn card leaving the given players stable

        Parameters:
            args:
                player: the player's whose stable it is
                card: the card to leave the stable
                played_card: the card to dictate the next move (if required)

    """
    player, card, played_card = args
    player.remove_card_from_stable(card)

    # Future states
    future_states = {
        "Barbed Wire": _apply_person_effect,
        "Black Knight Unicorn": _apply_person_effect,
        "Blinding Light": _apply_person_effect,
        "Blow Up Unicorn": _apply_person_effect,
        "Cupcakes For Everyone": _handle_share_upgrades,
    }

    if not(card.is_unicorn() and player.unicorn_effects_blocked):
        _move_next_state(card, future_states, [player, card])

    # Second round of states yolo. Mainly for blinding light to trigger any
    # remaining effects
    future_states = {
        "Blinding Light": _handle_check_unicorns_and_apply_states
    }
    _move_next_state(card, future_states, [player, card])

    # Other consequences
    if player.share_upgrades and card.is_upgrade():
        _handle_share_this_upgrade([player, card])

    if player.barbed_wire_effect:
        _handle_discard_card([player, None, None])

    if card.card_type == "Baby Unicorn":
        NURSERY.append(card)
        return


def _handle_look_at_hand(args):
    """ Handles the action of looking at the given players hand.

        Parameters:
            args:
                player: the player whose hand to look at
                played_card: the card to determine the next move
                    (if applicable)
                original_player: the player looking at the other players hand
    """
    player, played_card, original_player = args
    # print(f"Choose from: {player.hand}")
    # choice = int(input("Choice? ")
    choice = 0

    _handle_look_at_hand_choice_made(choice, args)


def _handle_look_at_hand_choice_made(choice, args):
    """ Handles the action of choosing a card from a players hand.

        Parameters:
            choice:
                the index of the chosen card
            args:
                player: the player losing the card
                played_card: the card to determine the next move
                    (if applicable)
                original_player: the player gaining (choosing) the card
    """
    player, played_card, original_player = args
    chosen_card = player.hand.pop(choice)
    original_player.add_to_hand(chosen_card)


def _handle_return_to_hand(args):
    # TODO: need to ensure this will be controlled by the correct player
    """ Handles the return to hand of a card (allows them to make a choice)

        Parameters:
            args:
                player: the owner of the hand being returned
                card: the card that dictates the next action
                original_player: the player doing the choosing (if required)

    """
    player, card, original_player = args
    # print(f"The possible cards are {player.stable}")
    # choice = input("Choose (number): ")
    choice = 0
    # Handling the return to hand
    _handle_return_to_hand_choice_made(choice, [player, card])

    future_states = {
        "Back Kick": _handle_discard_card
    }
    return _move_next_state(card, future_states, [player, card, None])


def _handle_return_to_hand_choice_made(choice, args):
    """ Handles the return of the chosen card to hand.

        Parameters:
            args:
                player: The player corresponding to the card being returned
                played_card: the card played to dictate the next state

     """
    player, played_card = args
    card = player.stable[choice]
    _handle_leave_stable([player, card, played_card])
    if card.card_type != "Baby Unicorn":
        _add_to_hand([player, card])


def _handle_sacrifice_or_destroy(args):
    """ Handles choosing whether to sacrifice or destroy when a choice
    is presented.

        Parameters:
            args:
                player: the player choosing whether to sacrifice or destroy
                card: the card to determine the next action
    """
    player, card = args
    # Currently the default assumption is to SACRIFICE a card.
    # (will test destroy later?)

    # choice = input("Sacrifice or destroy? (s/d) ")
    choice = "s"

    if choice == "s":
        return _handle_choose_card_sacrifice([player, card, None])
    else:
        return _handle_choose_card_destroy(args)


def _handle_sacrifice_this_card(args):
    """ Handles the sacrifice action of the given card.

        Parameters:
            args:
                player: the player sacrifice the card (owner of stable)
                card: the card being sacrificed
                played_card: the card that started this sacrifice and controls
                    possible future moves (if required)

        Returns:
            TRUE if win condition is met, otherwise FALSE
    """
    player, card, played_card = args

    c = None
    if card.is_unicorn() and player.unicorn_sacrifice_decoy:
        c = player.sacrifice_instead()
        _check_proceed_with_action([player, c, None])
    if c and c.location != CardLocation.STABLE:
        return

    # First the unicorn must leave the Stable
    _handle_leave_stable([player, card, None])

    # Attempt to return it to hand otherwise add to discard pile
    if card.return_to_hand:
        _add_to_hand(args)
        card.location = CardLocation.HAND
    else:
        DISCARD_PILE.append(card)
        card.location = CardLocation.DISCARD_PILE

    # Any further actions?
    future_work = {
        "Angel Unicorn": _choose_unicorn,
        "Cotton Candy Llamacorn": _handle_draw
    }

    # Fetch the possible cards if required for next action
    possible_cards = None
    if card == "Angel Unicorn":
        possible_cards = DISCARD_PILE
    result = player.has_won(WIN_NUMBER)
    result2 = _move_next_state(card, future_work,
                               [player, card, possible_cards])
    result3 = _move_next_state(played_card, future_work,
                               [player, card, possible_cards])
    result = result and result2 and result3
    return result


def _handle_search_deck(args):
    """ Handles searching the deck (namely finding the corresponding card).

    Could call a second method to determine card search if multiple matches

        Parameters:
            args:
                player: the player who is searching the deck
                card: the card that began the search
    """
    player, card = args
    search_term = {
        "Bear Daddy Unicorn": ("name", "Twinkicorn", True),
        "Classy Narwhal": ("type", "Upgrade", True)
    }
    possible_cards = _search_deck(search_term[card.name])

    # Need to make the choice
    # print(f"Possible cards are: {possible_cards}")
    # choice = int(input("Choice? "))
    choice = 0

    _handle_search_deck_choice(possible_cards[choice], args)

    # Need to shuffle deck
    random.shuffle(DECK)


def _handle_search_deck_choice(chosen_card, args):
    """ Handles the work once a choice has been made from the cards in the deck

        Parameters:
            chosen_card: the chosen card (Card type)
            args:
                player: the player making the choice
                played_card: the card that triggered the choice
                    (and determines the next action)

    """
    player, played_card = args

    # Find and remove the chosen card from the deck
    i = 0
    for card in DECK:
        if card == chosen_card:
            break
        i += 1
    DECK.pop(i)

    # What to do next?
    future_states = {
        "Bear Daddy Unicorn": _add_to_hand,
        "Classy Narwhal": _add_to_hand
    }

    _move_next_state(played_card, future_states, [player, chosen_card])


def _handle_share_upgrades(args):
    """ Handles sharing the current player's upgrades to all other players

        Parameters:
            player: the current player to search for upgrades
            played_card: the played card that determines the next state

        TODO: apply win condition!
    """
    player, played_card = args

    # For each player, apply the current effects
    upgrades = player.get_upgrades()
    for upgrade in upgrades:
        _handle_share_this_upgrade([player, upgrade])

    # Is there any future work to do?
    future_states = {
        "Cupcakes For Everyone": _apply_person_effect
    }
    _move_next_state(played_card, future_states, [player, played_card])


def _handle_share_this_upgrade(args):
    """ Handles sharing a particular upgrade with all other players.

        Parameters:
            player: the player sharing the upgrade
            upgrade: the upgrade to share

    """
    player, upgrade = args
    for other_player in PLAYERS:
        # Skip the current player, otherwise will turn off their effects
        if other_player == player:
            continue
        _apply_person_effect([other_player, upgrade])


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
        "A Cute Attack": _handle_a_cute_attack,
        "Back Kick": _choose_player,
        "Blatant Thievery": _choose_player
    }
    _move_next_state(card, future_work, [current_player, card])

    # Add to discard
    card.restore_defaults()
    card.location = CardLocation.DISCARD_PILE
    DISCARD_PILE.append(card)


def _remove_card_from_discard(card_to_remove):
    """ Removes the given card from the discard pile """
    index = 0
    for card in DISCARD_PILE:
        if card == card_to_remove:
            break
        index += 1
    return DISCARD_PILE.pop(index)


def _search_deck(args):
    """ Returns all the cards in the deck that match the given search term

        Parameters:
            args:
                matching_type: What part of the card are we searching
                matching_term: The term searching for
                exact: A boolean representing if an exact match is required

    """
    matching_type, matching_term, exact_match = args

    matches = []
    for card in DECK:
        if card.is_match(matching_type, matching_term, exact_match):
            matches.append(card)

    return matches


def _remove_unicorn_stop_effect_triggering(args):
    """ Turns off the card effect for the given card.

        Parameters:
            args:
                player: the player that owns the card (if applicable)
                unicorn: the card to turn the effect off
                played_card: the card that determines the next action
    """
    player, unicorn, played_card = args
    unicorn.effect_will_be_triggered = False
    future_work = {
        "A Cute Attack": _handle_leave_stable
    }
    # args = (current_player, card)
    _move_next_state(played_card, future_work, [player, unicorn, None])
    DISCARD_PILE.append(unicorn)


# Manages the turn: will return True if winning condition is met
def player_turn(current_player):

    # print(f"It is {current_player}")
    # Beginning of Turn Action
    _handle_beginning_turn_action(current_player)

    # Draw card
    _handle_draw([current_player, None, None])

    # Action phase
    # action = input("Action? ")
    won = False
    action = 0
    if action == "draw":
        _handle_draw([current_player, None, None])
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
        NURSERY.append(copy.copy(baby_unicorn))

    for player in player_names:
        PLAYERS.append(Player(player, copy.copy(baby_unicorn)))

    # Deal cards out
    for i in range(5):
        for player in PLAYERS:
            card = DECK.pop(0)
            player.add_to_hand(card)
