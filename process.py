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
    def deal_a_card(self):
        card_deal = self.deck.pop()
        return card(card_deal[0], card_deal[1])
class hand:
    def __init__(self, card_list, player):
        self.card_list = card_list
        self.player = player
        self.ace = False

        for card in self.card_list:
            if card.rank =="A":
                self.ace = True
    def get_score(self):
        total = 0
        for cards in self.card_list:
            total += cards.score
        return total
    def hit(self):
        new = card_deck.deal_a_card()
        self.card_list.append(new)
        if new.rank == "A":
            self.ace = True
    def bust_check(self):
        if self.get_score() > 21:
            print("{} busted".format(self.player))
            return True
        else:
            return False

        

    
