##
# colours.py
# Asks the user to pick a colour, compares it to another card
# returns if they guessed the correct colour.
# Abstracted by james

from random import choice, shuffle


def colours(partial_history):

    global BLACK_SUITS

    # Take the first character.
    # r if red, b if black
    choice = input("Red or Black? ").strip().lower()[0]

    print('-'*(len(partial_history)+2))
    print('', ''.join(partial_history))
    print('-'*(len(partial_history)+2))

    if choice == 'b' and partial_history[-1] in BLACK_SUITS:
        print('Correct!')
        multiplier = 2

    elif choice == 'r' and partial_history[-1] not in BLACK_SUITS:
        print('Correct!')
        multiplier = 2

    else:
        print("Incorrect!")
        multiplier = 0

    return multiplier

BLACK_SUITS = ['♤', '♧']  # Else theyre red
