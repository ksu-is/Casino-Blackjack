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
        print(self.suit + self.rank)