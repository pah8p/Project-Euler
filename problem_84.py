
import collections
import itertools
import random

class Monopoly(object):

    CHEST_CARDS = {
        1: 0,
        2: 10,
    }   

    CHANCE_CARDS = {
        1: 0,
        2: 10,
        3: 11,
        4: 24,
        5: 39,
        6: 5,
        7: 'next_rail',
        8: 'next_rail',
        9: 'next_utility',
        10: 'back_3',
    }

    def __init__(self, sides):
        self.double_run = 0
        self.chest_hit = 0
        self.chest_play = 0
        self.chance_hit = 0
        self.chance_play = 0
        self.times_on_square = collections.defaultdict(int)
        self.square = 0
        self.sides = sides
        self.chance_deck = shuffle_deck()
        self.chest_deck = shuffle_deck()
        
    def chest(self):
        card = self.chest_deck[0]
        self.chest_deck = self.chest_deck[1:] + [card]
        self.chest_play += 1
        try:
            self.square = self.CHEST_CARDS[card]
            if card == 2: self.chest_hit += 1
        except KeyError:
            pass
    
    def next_rail(self):
        if self.square == 7:
            return 15
        elif self.square == 22:
            return 25
        elif self.square == 36:
            return 5
    
    def next_utility(self):
        if self.square == 7:
            return 12
        elif self.square == 22:
            return 38
        elif self.square == 36:
            return 12

    def back_3(self):
        return self.square - 3

    def chance(self):
        card = self.chance_deck[0]
        self.chance_deck = self.chance_deck[1:] + [card]
        self.chance_play += 1
        if card == 2: self.chance_hit += 1
        try:
            card_result = self.CHANCE_CARDS[card]
            try:
                self.square = getattr(self, card_result)()
            except TypeError:
                self.square = card_result
        except KeyError:
            pass

    def play(self, n_rolls):
        n = 1
        while n < n_rolls:

            roll1 = random.randint(1, self.sides)
            roll2 = random.randint(1, self.sides)

            if roll1 == roll2:
                self.double_run += 1
            else:
                self.double_run = 0

            self.square = (self.square + roll1 + roll2) % 40

            if self.double_run == 3:
                self.square = 10
                self.double_run = 0
            elif self.square == 30:
                self.square = 10
            elif self.square in (2, 17, 33):
                self.chest()
            elif self.square in (7, 22, 36):
                self.chance()
                if self.square == 33:
                    self.chest()
     
            self.times_on_square[self.square] += 1

            n += 1

        return self.times_on_square
        
def shuffle_deck():

    deck = list(range(1, 17))
    shuffled_deck = []

    for i in range(16):

        card = random.randint(0, len(deck)-1)
        shuffled_deck.append(deck[card])
        deck.pop(card)

    return shuffled_deck
    
def roll_dice(sides):
    def _roll():
        return random.randint(1, sides+1) + random.randint(1, sides+1)
    return _roll


#for i in range(10): print(shuffle_deck())

game = Monopoly(6)

res = game.play(1000001)

##print(game.chest_play/game.chest_hit)
##print(game.chance_play/game.chance_hit)
##print(game.chance_deck)
##print(game.chest_deck)

print(sorted(res.items(), key=lambda x: x[1], reverse = True))



    
