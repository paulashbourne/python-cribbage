from card import Card

class PeggingCounter():

    def score(playedCards, newCard):
        points = 0

        if count == 15 or count == 31:
            points += 2

        points += pegNOfAKindPts(playedCards, newCard)
        points += pegRunPts(playedCards, newCard)
        return points

    def pegRunPts(playedCards, newCard)
        if len(playedCards) < 3:
            return 0
        cards = [p.rankInt for p in playedCards]
        cards.append(newCard.rankInt)
        cards.sort()
        run = True
        for i, c in enumerate(cards[1:]):
            if c - cards[i-1] != 1:
                run = False
                break
        if run:
            return len(cards)
        else:
            return pegRunPts(playedCards[1:], newCard)

    def pegNOfAKindPts(playedCards, newCard):
        numOfAKind = 1
        for p in reversed(self.cardsInPlay):
            if p.rankInt == newCard.rankInt:
                numOfAKind += 1
        if numOfAKind == 2:
            return 2
        elif numOfAKind == 3:
            return 6
        elif numOfAKind == 4:
            return 12
