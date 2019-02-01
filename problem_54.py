import collections

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Hand(object):
    def __init__(self, cards):
        self.cards = cards
        self.ranks = sorted([card.rank for card in cards])
        self.suits = [card.suit for card in cards]

        count = collections.defaultdict(int)
        for rank in self.ranks:
            count[rank] += 1
        self.count = count

    def _straight(self):
        for n in range(4):
            if not self.ranks[n] + 1 == self.ranks[n+1]:
                return False
        return True

    def _flush(self):
        return len(set(self.suits)) == 1

    def _four_of_kind(self):
        for rank, counts in self.count.items():
            if counts == 4:
                return True, rank
        return False, None

    def _three_of_kind(self):
        for rank, counts in self.count.items():
            if counts == 3:
                return True, rank
        return False, None

    def _two_of_kind(self):
        pairs = []
        for rank, counts in self.count.items():
            if counts == 2:
                pairs.append(rank)

        if pairs:
            return True, max(pairs), min(pairs), len(pairs)
        else:
            return False, None, None, None

    def _two_pair(self):
        flag, hi, lo, n = self._two_of_kind()
        if flag and n == 2:
            return True, hi, lo
        else:
            return False, None, None

    def _one_pair(self):
        flag, hi, lo, n = self._two_of_kind()
        if flag and n == 1:
            return True, hi
        else:
            return False, None

    def _high_card(self):
        solos = []
        for rank, counts in self.count.items():
            if counts == 1:
                solos.append(rank)
        return max(solos)

    def rank(self):

        if self._straight() and self._flush():
            return 90 + self.ranks[-1]/10

        elif self._four_of_kind()[0]:
            return 80 + self._four_of_kind()[1]/10

        elif self._three_of_kind()[0] and self._two_of_kind()[0]:
            return 70 + self._three_of_kind()[1]/10

        elif self._flush():
            return 60 + self.ranks[-1]/10

        elif self._straight():
            return 50 + self.ranks[-1]/10

        elif self._three_of_kind()[0]:
            return 40 + self._three_of_kind()[1]/10

        elif self._two_pair()[0]:
            return 30 + self._two_pair()[1]/10 + self._two_pair()[2]/100

        elif self._one_pair()[0]:
            return 20 + self._one_pair()[1]/10 + self._high_card()/100

        else:
            return 10 + self.ranks[-1]/10

def load_games():
    file = 'C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p054_poker.txt'
    with open(file, 'r') as f:
        raw_hands = f.readlines()

    def _clean_rank(n):
        if n == 'T':
            return 10
        elif n == 'J':
            return 11
        elif n == 'Q':
            return 12
        elif n == 'K':
            return 13
        elif n == 'A':
            return 14
        else:
            return int(n)

    games = []
    for x in raw_hands:
        hand_1 = Hand([
            Card(_clean_rank(x[0]), x[1]),
            Card(_clean_rank(x[3]), x[4]),
            Card(_clean_rank(x[6]), x[7]),
            Card(_clean_rank(x[9]), x[10]),
            Card(_clean_rank(x[12]), x[13]),
        ])
        hand_2 = Hand([
            Card(_clean_rank(x[15]), x[16]),
            Card(_clean_rank(x[18]), x[19]),
            Card(_clean_rank(x[21]), x[22]),
            Card(_clean_rank(x[24]), x[25]),
            Card(_clean_rank(x[27]), x[28]),
        ])
        games.append((hand_1, hand_2))
    return games

hand_1 = Hand([
    Card(2, 'H'),
    Card(2, 'D'),
    Card(4, 'C'),
    Card(4, 'D'),
    Card(4, 'S'),
])

hand_2 = Hand([
    Card(3, 'C'),
    Card(3, 'D'),
    Card(3, 'S'),
    Card(9, 'S'),
    Card(9, 'D'),
])

print(hand_2.rank() > hand_1.rank())
print(hand_2.rank())
print(hand_1.rank())


games = load_games()
hand_1_wins = [1 for game in games if game[0].rank() > game[1].rank()]
print(sum(hand_1_wins))








