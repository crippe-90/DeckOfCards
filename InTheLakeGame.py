#author: Christoffer Norell
#contact: christoffernorell@yahoo.se
#The game file for In the lake.

import DeckOfCards
import InTheLake


#Get a new shuffled deck of cards.
deck = DeckOfCards.Deck()
deck.shuffle()

#Hand seven cards to each player.
player = InTheLake.Player(deck.hand_cards(7))
oponent = InTheLake.OponentAI(deck.hand_cards(7))

#Shake hands to get a reference to eachother.
player.shake_hand(oponent)
oponent.shake_hand(player)

#Start the game.
game_running = True
while(game_running):
    print("you currently have :")
    sorted_hand = player.get_sorted_hand()
    for cards in sorted_hand:
        for card in cards:
            print(card.show())
    
    valid_card = False
    while not valid_card:
        cards_asked_for = input("Ask for cards from your oponent:")
        for cards in deck.valid_cards:
            if cards_asked_for.lower()==cards.split(' ')[1]:
                valid_card = True
        print("You asked for " + cards_asked_for)


    game_running = False
