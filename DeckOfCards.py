#author: Christoffer Norell
#contact: christoffernorell@yahoo.se

#This is a simple simulator of a deck of cards I made for fun.
#The values in the dictionaries are there for better comparison during games.


import random
#Using dictionaries to represent values.
#The color-values was taken from bridge-order:
#http://pokerterms.com/bridge-order.html

colors = [{'Hearts': 0 },{'Diamonds': 1},{'Clubs': 2},{'Spades':3}]
values = [{'Two':2},{'Three': 3},{'Four':4},{'Five':5},{'Six': 6},{'Seven': 7}, {'Eight': 8}, {'Nine': 9} , {'Ten': 10},{'Jack': 11} , {'Queen':12}, {'King':13}
, {'Ace':14}]


class Card():
    def __init__(self,color,value):
        self.color = color
        self.value = value

    def show(self):
        return list(self.color.keys())[0] + ' ' + list(self.value.keys())[0]

    def get_value(self):
        return list(self.value.values())[0]
    
    def get_color_value(self):
        return list(self.color.value())[0]
    


class Deck():
    def __init__(self):
        self.deck = []
        self.valid_cards = []
        for x in range(len(colors)):
            for y in range(len(values)):
                card = Card(colors[x],values[y])
                self.deck.append(card)
                self.valid_cards.append(card.show().lower())
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def hand_card(self):
        card = self.deck.pop()
        return card
    
    def hand_cards(self, amount):
        tmp = []
        if amount <= len(self.deck):
            for x in range(amount):
                tmp.append(self.hand_card())
            return tmp
        else:
            print("out of cards")
            return None

