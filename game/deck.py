from card import Card

class Deck():

    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def append(self, card):
        self.cards.append(card)

    def prepend(self, card):
        self.cards.insert(0, card)

    def extend(self, cards):
        self.cards.extend(cards)

    def shuffle(self):
        newDeck = list(self.cards)
        while self.cards:
            newDeck.append(self.cards[randrange(len(self.cards))])
        self.cards = newDeck

    def sort(self):
        self.cards.sort()

    def reset(self):
        self.cards = [Card(v) for v in range(52)]

    def pop(self, idx=-1):
        return self.cards.pop(idx)

    def remove(self, value):
        return self.cards.remove(value)
