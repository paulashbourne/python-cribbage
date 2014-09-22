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
