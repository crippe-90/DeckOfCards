#author: crippe-90 @github

#Classes for player and oponent in the game "In the Lake".
import random

#Player class
class Player():
    def __init__(self, cards=[]):
        self.cards = cards
        self.fours = 0
        self.sorted_hand = []
        self.sort_cards()

    #Sorting cards in the beginning because we want to have four of each value.
    def sort_cards(self):
        x=2
        self.sorted_hand = []
        while(x<=15):
            tmp = []
            for card in self.cards:
                if card.get_value()==x:
                    tmp.append(card)
            self.sorted_hand.append(tmp)
            x+=1
    
    def get_hand(self):
        return self.cards
    #returns the sorted hand.
    def get_sorted_hand(self):
        return self.sorted_hand
    
    #return cards asked for by the oponent
    def give_cards(self, cards_to_give=""):
        tmp = []
        for card in self.cards:
            if card.show().split(' ')[1].lower()==cards_to_give.lower():
                tmp.append(card)
        for card in tmp:
            self.cards.remove(card)
        return tmp
  
    #hands the requested cards if they are in oponents hand.
    def hand_cards(self, requested_cards):
        cards_to_give = []
        for card in self.cards:
            if requested_cards.lower()==card.show().split(' ')[1].lower():
                cards_to_give.append(self.give_cards(card.show().split(' ')[1].lower()))
        return cards_to_give


#OponentAI
class OponentAI(Player):
    def __init__(self,cards=[]):
         Player.__init__(self, cards)

    def remove_cards_from_sorted_hand(self):
        sorted_hand = self.sorted_hand
        for x in range(len(sorted_hand)):
            if len(sorted_hand[x])==4:
                self.sorted_hand.pop(x)

    #Returning the cards that are closest to four.
    def get_cards_closest_to_four(self):
        for cards in self.sorted_hand:
            if len(cards)==3:
                return cards
                
        for cards in self.sorted_hand:
            if len(cards)==2:
                return cards

        for cards in self.sorted_hand:
            if len(cards)==1:
                return cards
           

    
    




