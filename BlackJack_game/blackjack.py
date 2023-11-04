Cette version du programme utilise des fonctions pour simplifier le code, permet de gérer les Aces de manière appropriée (1 point ou 11 points), et suit un flux plus logique pour le jeu. 

# BLACK JACK - CASINO

import random

def deal_card(deck, hand, num_cards):
    for _ in range(num_cards):
        card = deck.pop()
        hand.append(card)
    return hand

def calculate_total(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        visible_cards = ['X'] + hand[1:]
    else:
        visible_cards = hand
    print("The cards are", visible_cards)
    print("The total is", calculate_total(hand))

def blackjack_winner(player_total, dealer_total):
    if player_total > 21:
        return "Dealer"
    if dealer_total > 21:
        return "Player"
    if player_total == dealer_total:
        return "Tie"
    return "Player" if player_total > dealer_total else "Dealer"

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(deck)

dealer_hand = []
player_hand = []

dealer_hand = deal_card(deck, dealer_hand, 2)
player_hand = deal_card(deck, player_hand, 2)

print("Welcome to the game Casino - BLACK JACK!")
display_hand(dealer_hand, hide_first_card=True)
display_hand(player_hand)

if calculate_total(player_hand) == 21:
    print("Blackjack! Player wins!")
else:
    while calculate_total(player_hand) < 21:
        choice = input("Do you want to hit or stay? (1 for hit, 0 for stay): ")
        if choice == "1":
            player_hand = deal_card(deck, player_hand, 1)
            display_hand(player_hand)
        else:
            break

    while calculate_total(dealer_hand) < 17:
        dealer_hand = deal_card(deck, dealer_hand, 1)

    display_hand(dealer_hand)
    winner = blackjack_winner(calculate_total(player_hand), calculate_total(dealer_hand))
    print("{winner} wins!")
