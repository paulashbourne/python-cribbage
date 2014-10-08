from deck import Deck

class Hand(Deck):

    def __init__(self, crib=False):
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

    @property
    def minCard(self):
        v = 100
        for c in self.cards:
            if c.rankInt < v:
                v = c.rankInt
        return v
