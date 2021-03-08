import random
colors = ['Hearts','Diamonds','Clubs','Spades']
values = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King', 'Ace']

class Card():
    def __init__(self,value,color):
        self.color = color
        self.value = value

    def show(self):
        return (self.color, self.value)


class Deck():
    def __init__(self):
        self.deck = []
        for x in range(len(colors)):
            for y in range(len(values)):
                self.deck.append(Card(colors[x],values[y]))
    
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

deck = Deck()
deck.shuffle()

cards = deck.hand_cards(52)

for c in cards:
    print(c.show())