suits = ['heart', 'diamonds', 'spades', 'clubs']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card (object):
  def __init__(self,suit,value):
    self.suits = suit
    self.values = value

class Deck(object):
  def __init__(self):
    self.cards = []
    for suit in suits:
        for value in values:
          self.cards.append(Card(suit, value))
    print self.cards

our_deck = Deck()
