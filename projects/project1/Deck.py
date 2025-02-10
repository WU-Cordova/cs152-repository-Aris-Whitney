from bag import Bag
from Card import Card, Suit, Face
import random
import copy
class MultiDeck():
    def __init__(self):
        one_deck_list = [Card(face, suit) for suit in Suit for face in Face]

        self.deck_count = random.choice([2, 4, 6, 8])
        multi_deck_list = [card for _ in range(self.deck_count) for card in copy.deepcopy(one_deck_list)]

        self.deck_bag = Bag(*multi_deck_list)
    def DrawRand(self):
        if len(self.deck_bag.items) > 0:
            current_card = random.choice(self.deck_bag.items)
            self.deck_bag.remove(current_card)  # Remove the drawn card from the deck
            return current_card
        else:
            raise ValueError("The deck is empty!")
        
        

