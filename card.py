class Card():
    RANK_SYMBOLS = [
        'A',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'J',
        'Q',
        'K'
    ]
    RANK_NAMES = [
        'Ace',
        'Two',
        'Three',
        'Four',
        'Five',
        'Six',
        'Seven',
        'Eight',
        'Nine',
        'Ten',
        'Jack',
        'Queen',
        'King'
    ]
    SUIT_SYMBOLS = [
        '♥',
        '♦',
        '♣',
        '♠'
    ]
    SUIT_NAMES = [
        'Hearts',
        'Diamonds',
        'Clubs',
        'Spades'
    ]
    SUIT_UNICODE_CHARS = [
        'a',
        'b',
        'c',
        'd'
    ]

    def __init__(self, value):
        self.value = value
        return self

    def __cmp__(self, obj):
        if not obj or self.rankInt > obj.rankInt:
            return 1
        elif self.rankInt < obj.rankInt:
            return -1
        else:
            if self.value == obj.value:
                return 0
            elif self.suitInt > obj.suitInt:
                return -1 # intentional
            else:
                return 1

    @property
    def suitInt(self):
        return self.value / 13

    @property
    def rankInt(self):
        return self.value % 13

    @property
    def suitSymbol(self):
        return Card.SUIT_SYMBOLS[self.suitInt]

    @property
    def rankSymbol(self):
        return Card.RANK_SYMBOLS[self.rankInt]

    @property
    def suitName(self):
        return Card.SUIT_NAMES[self.suitInt]
        
    @property
    def rankSymbol(self):
        return Card.RANK_NAMES[self.rankInt]

    @property
    def unicodeCard(self):
        s = '\xf0\x9f\x82\xae'
        s += Card.SUIT_UNICODE_CHARS[self.suitInt]
        if self.rankInt < 10:
            s += self.rankInt
        else:
            c = ['a','b','c','d']
            s += c[self.rankInt]
        return s

    @property
    def symbolString(self):
        return "%s%s" % (self.rankSymbol, self.suitSymbol)

    @property
    def nameString(self):
        return "%s of %s" % (self.rankName, self.suitName)

class Deck():

    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def append(self, card):
        self.cards.append(card)

    def prepend(self, card):
        self.card.insert(0, card)

    def shuffle(self):
        newDeck = list(self.cards)
        while self.cards:
            newDeck.append(self.cards[randrange(len(self.cards))])
        self.cards = newDeck

    def sort(self):
        self.cards.sort()

class Hand(Deck):

    def __init__(crib=False):
        self.crib = crib
        self.cards = []

    @static
    def fifteenPts(ranklist, subset=None):
        count = 0
        if not subset:
            for a in range(len(ranklist)):
                for b in range(a, len(ranklist)):
                    subset = [ranklist[a], ranklist[b]]
                    count += fifteenPts(ranklist[b+1:], subset)
        else:
            s = sum(subset)
            if subset == 15:
                count+=1
            elif subset < 15 and len(ranklist) > 0:
                for c in range(len(ranklist)):
                    newsubset = list(subset)
                    newsubset.append(ranklist[c])
                    count += fifteenPts(ranklist[c+1:], newsubset)
        return count * 2

    @static
    def runPts(ranklist, num=5):
        count = 0
        ranklist.sort()
        for combination in itertools.combinations(ranklist, num):
            run = True
            for x in range(1, len(combination)):
                if combination[x] - combination[x-1] != 1:
                    run = False
                    break
            if run:
                count+=len(combination)
        if count == 0 and num > 3:
            #check for smaller runs
            count += runPts(ranklist, num - 1)
        return count

    def knobsPts(self, upcard):
        for card in self.cards:
            if card.rankInt == 10 and card.suitInt == upcard.suitInt:
                return 1
        return 0

    def flushPts(self, upcard):
        # All four cards in hand must be same suit for a flush
        # If hand is a crib, then the upcard must also be same suit
        for i in range(1, len(self.cards)):
            if self.cards[i].suitInt != self.cards[i-1].suitInt:
                return 0
        if upcard.suitInt == self.cards[0].suitInt:
            return 5
        elif is crib:
            return 0
        else:
            return 4

    def score(self, upcard):
        if len(self.cards) != 4:
            return False
        temphand = list(self.cards).append(upcard)
        ranklist = [c.rankInt for c in temphand]
        score = self.countFifteens(ranklist)
        score += self.runPts(ranklist)
        score += self.nobsPts(upcard)
        score += self.flushPts(upcard)
        return score
