#author: Christoffer Norell
#contact: christoffernorell@yahoo.se

#A text version of a swedish card game for children.
#Original title in swedish is "Finns i sjön".

#Rules:
#Every player gets seven cards on hand. The rest of the cards are spread in the lake.
#Now you need to collect four's. You do this by asking your oponends after the cards you wish to have.
#When you have four cards of a given value you get one point. The one who gets most points when the game is over has won.
#If you get out of cards you pick 7 new ones, if the lake is empty you have to wait for the next game.

#Rules on swedish: https://www.spelregler.org/finns-i-sjon/
class Player():
    def __init__(self, cards=[]):
        self.cards = cards
        self.fours = 0
        self.sorted_hand = []
        self.oponent = None

        self.sort_cards()

    def shake_hand(self,oponent):
        self.oponent = oponent


    #Sorting cards in the beginning because we want to have four of each value.
    def sort_cards(self):
        x=2
        while(x<15):
            tmp = []
            for card in self.cards:
                if card.get_value()==x:
                    tmp.append(card)
            self.sorted_hand.append(tmp)
            x+=1
    
    #returning the amount of fours.
    def get_fours(self):
        for cards in self.sorted_hand:
            if len(cards)==4:
                self.fours+=1
        return self.fours

    #returns the sorted hand.
    def get_sorted_hand(self):
        return self.sorted_hand
    
    #return cards asked for by the oponent
    def give_cards(self, cards_value=0):
        for cards in self.sorted_hand:
            if len(cards)>1:
                if cards[0].get_value()==cards_value:
                    tmp = cards
                    self.sorted_hand.remove(cards)
                    return tmp

    #requesting cards from the oponent
    def get_cards(self, value):
        tmp = self.oponent.give_cards(value)
        for cards in self.sorted_hand:
            if len(cards)>1:
                if cards[0].get_value()==tmp[0].get_value():
                    cards.append(tmp)
                    return
                else:
                    print("asking for cards not in hand.")
                    return
            
        print("does not have card")




class OponentAI(Player):
    def __init__(self,cards=[]):
        self.cards = cards
        Player.__init__(self, self.cards)    

    #returning the cards that are closest to four
    def get_cards_closest_to_four(self):
        for cards in self.sorted_hand:
            if len(cards)==4:
                return cards
        for cards in self.sorted_hand:
            if len(cards)==3:
                return cards
        for cards in self.sorted_hand:
            if len(cards)==2:
                return cards
        return self.sorted_hand[0]

    #requesting cards from player
    def request_cards(self):
        cards = self.get_cards_closest_to_four()
        self.oponent.get_cards(cards[0].cards_value())



