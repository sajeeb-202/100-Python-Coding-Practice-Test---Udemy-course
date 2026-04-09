import random
from itertools import product

def create_deck():
   
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    deck = list(product(ranks, suits))
    return deck


def shuffle_deck(deck):
    
    shuffled_deck = deck.copy()
    random.shuffle(shuffled_deck)
    return shuffled_deck