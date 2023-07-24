#author: crippe-90 @github

#A text version of a swedish card game for children. Currently supporting 1 player + computer.
#Original title in swedish is "Finns i sjön".

#Rules:
#Every player gets seven cards on hand. The rest of the cards are spread in the lake.
#Now you need to collect four's. You do this by asking your oponents after the cards you wish to have.
#When you have four cards of a given value you get one point. The one who gets most points when the game is over has won.
#If you get out of cards you pick 7 new ones, if the lake is empty you have to wait for the next game.

#Rules on swedish: https://www.spelregler.org/finns-i-sjon/



from .InTheLakePlayers import *
from .DeckOfCards import Deck

class Game():
    
    def __init__(self):
        #Get a new shuffled deck of cards.
        self.deck = Deck()
        self.deck.shuffle()
        self.game_running = True
        #Hand seven cards to each player.
        self.player = Player(self.deck.hand_cards(7))
        self.oponent = OponentAI(self.deck.hand_cards(7))
        #Create a referee to keep track of points
        self.referee = Referee(oponent=self.oponent, player=self.player)

    #Shows the current cards of the hand
    def show_current_cards(self, who, hand):
        print(who + " currently have theese cards:")
        cards_in_hand = ""
        for card in hand:
            cards_in_hand += card.show() + "\n"
        print(cards_in_hand)

    #Asks the computer for a card
    #Method functionality should be moved to InTheLakePlayers module
    def ask_for_card(self, who='Someone'):
        valid_card = False
        while not valid_card:
            cards_asked_for = input(who + ", Ask for cards from your oponent:")
            for cards in self.deck.valid_cards:
                if cards_asked_for.lower()==cards.split(' ')[1]:
                    valid_card = True
            print(who + " asked for " + cards_asked_for)
        self.check_if_oponent_has_card(cards_asked_for)


    #Draws the top card from the deck
    def draw_card_from_deck(self):
        return self.deck.hand_card()

    #The computer checks if it has the cards
    #Method-functionality shouldd be moved to player-class
    def check_if_oponent_has_card(self, cards):
        cards_to_give_player = self.oponent.hand_cards(cards)
        if cards_to_give_player:
            for cards in cards_to_give_player:
                for card in cards:
                    self.player.cards.append(card)
        else:
            print("Card is in the lake!")
            self.player.cards.append(self.draw_card_from_deck())

    #Oponent asks for a card
    #Method-functionality should be moved to oponentAI-class
    def oponent_ask_for_card(self):
        cards_to_ask_for = self.oponent.get_cards_closest_to_four()
        if cards_to_ask_for==None:
            self.game_running = False
            return
        card_to_ask_for = cards_to_ask_for[0].show().split(' ')[1]
        print("Oponent asks for: " + card_to_ask_for)
        self.check_if_player_has_card(card_to_ask_for)
        
    #Method-functionality should be moved to player-class
    def check_if_player_has_card(self, cards):
        cards_to_hand_oponent = self.player.hand_cards(cards)
        if cards_to_hand_oponent:
            for cards in cards_to_hand_oponent:
                for card in cards:
                    self.oponent.cards.append(card)
        else:
            print("Card is in the lake!")
            self.oponent.cards.append(self.draw_card_from_deck())


    #Run the game.
    def main_loop(self):
        turn = 1
        print("\n****** GAME STARTS ******\n")
        while(not self.deck.empty() and self.game_running is True):
            print("\n****** NEW TURN ******\n")
            print("TURN " + str(turn))
            self.show_current_cards("Player", self.player.get_hand())
            #self.show_current_cards("Oponent",self.oponent.get_hand())
            
            if self.deck.empty() is False:
                self.ask_for_card("Player")
                self.player.sort_cards()
                self.oponent.sort_cards()
                self.referee.count_points()
            print("******")
            input("Now it is oponents turn, press enter to continue.")
            self.show_current_cards("Player",self.player.get_hand())
            #self.show_current_cards("Oponent",self.oponent.get_hand())
            
            if self.deck.empty() is False:
                self.oponent_ask_for_card()
                input("Oponent is done, press enter to continue")
                self.player.sort_cards()
                self.oponent.sort_cards()
                self.referee.count_points()
            turn += 1
        self.referee.declare_winner()




class Referee():
    def __init__(self,player=None, oponent=None):
        self.player = player
        self.oponent = oponent
        self.player_points = 0
        self.oponent_points = 0

    def count_points(self):
        player_sorted_hand = self.player.get_sorted_hand()
        oponent_sorted_hand = self.oponent.get_sorted_hand()
        for cards in player_sorted_hand:
            if len(cards)==4:
                print("POINTS TO PLAYER!")
                self.player_points += 1
                self.player.sorted_hand.remove(cards)
                for card in cards:
                    self.player.cards.remove(card)
        for cards in oponent_sorted_hand:
            if len(cards)==4:
                print("POINTS TO OPONENT!")
                self.oponent_points+=1
                self.oponent.sorted_hand.remove(cards)
                for card in cards:
                    self.oponent.cards.remove(card)
                    self.oponent.remove_cards_from_sorted_hand()
       

    def declare_winner(self):
        text = "The winnes is... "
        if self.player_points > self.oponent_points:
            text += "Player! \nPlayer: " +  str(self.player_points) + " Oponent: " + str(self.oponent_points)

        elif self.player_points < self.oponent_points:
            text += "Oponent! \nPlayer: "  +  str(self.player_points) + " Oponent:" + str(self.oponent_points)
        else:
            text = "It's a draw!\n Player gets: " + str(self.player_points) + " Oponent gets: " + str(self.oponent_points)
        print("Referee: " + text)


