from os import system
import random

class card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        if rank == "K" or rank == "Q" or rank =="J":
            self.score = 10
        elif rank == "A":
            self.score = 1
        else:
            self.score = int(rank)
    def show(self):
        print(self.suit + self.rank)

class dealer_deck:
    def __init__(self, deck):
        self.deck = deck
    def count(self):
        return len(self.deck)
    def display_deck(self):
        for suit,rank in self.deck:
            c = card(suit, rank)
            c.show()
    def create_deck(self):
        self.deck = []
        for suit in suit.list:
            for rank in rank.list:
                self.deck.append((suit,rank))
    def shuffle_deck(self):
        system("clear")
        print("Dealer Shuffling")
        random.shuffle(self.deck)
        

    