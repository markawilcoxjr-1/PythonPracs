import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card1 = random.choice(deck)
card2 = random.choice(deck)
card3 = random.choice(deck)
card4 = random.choice(deck)
player_hand = [card1, card2]
dealer_hand = [card3, card4]

print("Welcome to PYjack 21!")

def game_bj():
    print("Dealer: ", dealer_hand[0])
    print("\nPlayer: ", player_hand)
    player_choice = input("\nHit or Stay?! Type 'h' if hit or type 's' if you want to stay: \n")
    if player_choice == "h":
        if card1 + card2 > 21:
        game_over = True
    while not game_over:



game_bj()