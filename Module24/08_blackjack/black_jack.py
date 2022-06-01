import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_card(self):
        card = self.value + " of " + Deck.suits[self.suit]
        return card


class Deck:
    suits = {'S': "Spades", "C": "Clubs", "H": "Hearts", "D": "Diamonds"}
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                   '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        self.deck = [Card(suit, key)
                     for suit in self.suits
                     for key in self.card_values]

    def deck_shuffle(self):
        random.shuffle(self.deck)

    def take_card(self):
        return self.deck.pop(0)


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, *args):
        for arg in args:
            self.hand.append(arg)

    def show_hand(self):
        print(f"{self.name}, у вас на руках: ", end='')
        player_hand = [card.show_card() for card in self.hand]
        print(", ".join(player_hand))

    def calc_score(self):
        score = [Deck.card_values[card.value] for card in self.hand]
        return sum(score)
