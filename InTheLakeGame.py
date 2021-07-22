#author: Christoffer Norell
#contact: christoffernorell@yahoo.se

#The game file for In The Lake. currently under development

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

#Shows the current cards that the player has
def show_current_cards(who, hand):
    print(who + " currently have :")
    for card in hand:
        print(card.show())

#Asks the computer for a card
def ask_for_card(who_asked='Someone'):
    valid_card = False
    while not valid_card:
        cards_asked_for = input(who_asked + ", Ask for cards from your oponent:")
        for cards in deck.valid_cards:
            if cards_asked_for.lower()==cards.split(' ')[1]:
                valid_card = True
        print("You asked for " + cards_asked_for)
    check_if_oponent_has_card(cards_asked_for)




#The computer checks if it has the cards
def check_if_oponent_has_card(cards):
    cards_to_give_player = oponent.hand_cards(cards)
    for cards in cards_to_give_player:
        for card in cards:
            player.cards.append(card)
   
#Run the game.
game_running = True
while(game_running):
    show_current_cards("Player", player.get_hand())
    show_current_cards("Oponent",oponent.get_hand())
    ask_for_card("Player")
    show_current_cards("Player",player.get_hand())
    show_current_cards("Oponent",oponent.get_hand())
    
    game_running = False
