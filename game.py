##
# game.py
# GAmbling
# DAgo Wrotten, James Abstracted, Planned together
from random import choice, shuffle
from colours import *
from suits import *

# Gambling imports return bool and multiplier.


# Set up cards
def setup_cards():
    SUITS = ['♤', '♡', '♧', '♢']
    CARDS_PER_SUIT = 13
    deck = []

    for card in range(CARDS_PER_SUIT):
        for suit in SUITS:
            deck.append(suit)

    shuffle(deck)

    return deck

deck = setup_cards()

suit_history = []
HISTORY_MAX = 6


# "yes" responses. Lowercase
AFFIRMATIVES = ['y', 'ye', 'yes', 'yeah', 'sure', 'r', 'b', '']

message = "Would you like to gamble? You current balance is ${}. "

# Fill history
for i in range(0, HISTORY_MAX):
    # Pick card
    suit_history.append(deck.pop())

# Set up loop
balance = 100
playing = True

while playing and balance > 0:
    if len(deck) <= 0:
        deck = setup_cards()

    playing = (True if input(message.format(balance)).strip().lower()
               in AFFIRMATIVES else False)

    if not playing:
        continue

    print('-'*(HISTORY_MAX+2))
    print('', ''.join(suit_history[-HISTORY_MAX:]))
    print('-'*(HISTORY_MAX+2))

    # Pick card
    suit_history.append(deck.pop())

    # Asks the user what method of gambling they would like to partake in.
    # c for colour, s for suits
    bet_choice = input("Would you like to bet on the colour"
                       " or suit of the card? ").strip().lower()[0]

    if bet_choice == 'c':
        balance *= colours(suit_history[-HISTORY_MAX:])

    elif bet_choice == 's':
        balance *= suits(suit_history[-HISTORY_MAX:])

    else:
        print("Not a valid option")

print("Your final balance is ${}.".format(balance))
