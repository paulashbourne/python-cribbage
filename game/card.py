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
        "\xe2\x99\xa5",
        "\xe2\x99\xa6",
        "\xe2\x99\xa3",
        "\xe2\x99\xa0",
    ]
    SUIT_NAMES = [
        'Hearts',
        'Diamonds',
        'Clubs',
        'Spades'
    ]
    UNICODE_CARDS = [
        '\xf0\x9f\x82\xa1', '\xf0\x9f\x82\xa2', '\xf0\x9f\x82\xa3','\xf0\x9f\x82\xa4', '\xf0\x9f\x82\xa5', '\xf0\x9f\x82\xa6', '\xf0\x9f\x82\xa7', '\xf0\x9f\x82\xa8', '\xf0\x9f\x82\xa9', '\xf0\x9f\x82\xaa', '\xf0\x9f\x82\xab', '\xf0\x9f\x82\xac', '\xf0\x9f\x82\xad', '\xf0\x9f\x82\xb1', '\xf0\x9f\x82\xb2', '\xf0\x9f\x82\xb3', '\xf0\x9f\x82\xb4', '\xf0\x9f\x82\xb5', '\xf0\x9f\x82\xb6', '\xf0\x9f\x82\xb7', '\xf0\x9f\x82\xb8', '\xf0\x9f\x82\xb9', '\xf0\x9f\x82\xba', '\xf0\x9f\x82\xbb', '\xf0\x9f\x82\xbc', '\xf0\x9f\x82\xbd', '\xf0\x9f\x82\xc1', '\xf0\x9f\x82\xc2', '\xf0\x9f\x82\xc3', '\xf0\x9f\x82\xc4', '\xf0\x9f\x82\xc5', '\xf0\x9f\x82\xc6', '\xf0\x9f\x82\xc7', '\xf0\x9f\x82\xc8', '\xf0\x9f\x82\xc9', '\xf0\x9f\x82\xca', '\xf0\x9f\x82\xcb', '\xf0\x9f\x82\xcc', '\xf0\x9f\x82\xcd', '\xf0\x9f\x82\xd1', '\xf0\x9f\x82\xd2', '\xf0\x9f\x82\xd3', '\xf0\x9f\x82\xd4', '\xf0\x9f\x82\xd5', '\xf0\x9f\x82\xd6', '\xf0\x9f\x82\xd7', '\xf0\x9f\x82\xd8', '\xf0\x9f\x82\xd9', '\xf0\x9f\x82\xda', '\xf0\x9f\x82\xdb', '\xf0\x9f\x82\xdc', '\xf0\x9f\x82\xdd'
    ]

    def __init__(self, value):
        self.value = value

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
    def symbolString(self):
        return "%s%s" % (self.rankSymbol, self.suitSymbol)

    @property
    def nameString(self):
        return "%s of %s" % (self.rankName, self.suitName)
