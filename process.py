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
    def bj_check(self):
        if (self.get_score() == 10 and len(self.card_list) == 2 and self.ace is True):
            return True
        else:
            return False
def game_state(player_cond, dealer_cond):
    system("clear")
    dealer_hand.show_hand(dealer_cond)
    score = dealer_hand.get_score()
    bust = dealer_hand.bust_check()
    if dealer_hand.bj_check() is True and dealer_cond is False:
        print("Dealer Has Blackjack")
    elif (dealer_cond is False and dealer_hand.ace is True and bust is False and score + 10 < 22):
        print("Total: " + str(score) + "or" + str(score + 10))
    elif dealer_cond is False:
        print("Total: " + str(score))
    plyr_hand.show_hand(player_cond)
    score = plyr_hand.get_score()
    plyr_hand.bust_check()
    if plyr_hand.bj_check() is True:
        print("You have Blackjack")
    elif plyr_hand.ace() is True and bust is False and score + 10 < 22):
        print("Total: " + str(score) + "or" + str(score + 10))
    else:
        print("Total: " + str(score))



suit_list = [heart, club, spade, diamond]
pic_cards = ["J", "Q", "K", "A"]
rank_list = [str(x) for x in range(2, 11)] + pic_cards

card_deck = dealer_deck([])
card_deck.new_deck()
card_deck.shuffle_deck()
        

        

    
