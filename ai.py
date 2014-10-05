from card import card
from hand import hand
from copy import copy
from peggingCounter import PeggingCounter

class AI():

    @staticmethod
    def getDepositCards(hand, playercrib):
        availableCards = Deck()
        availableCards.reset()
        for c in self.cards:
            availableCards.remove(c)
        # Consider every combination of cards thrown away
        combinations = []
        maxComb = {'weighted' : -1000}
        for dropCards in itertools.combinations(hand, 2):
            comb = {
                'cards'     : dropCards,
                'avgHand'   : 0,
                'avgCrib'   : 0,
                'weighted'  : 0
             }
            _hand = copy(hand)
            _hand.remove(dropCards[0])
            _hand.remove(dropCards[1])
            crib = Hand()
            crib.extend(dropCards)
            for upcard in availableCards:
                _availableCards = copy(availableCards)
                _availableCards.remove(upcard)
                comb['avgHand'] += _hand.score(upcard)
                cribCombCount = 0
                for otherCribCards in \
                        itertools.combinations(_availableCards, 2):
                    comb['avgCrib']
                    _crib = copy(_crib)
                    _crib.extend(otherCribCards)
                    comb['avgCrib'] += _crib.score(upcard)
                comb['avgCrib'] /= float(combCount)
            total = float(len(availableCards))
            comb['avgHand'] /= total
            comb['avgCrib'] /= total
            comb['weighted'] = comb['avgHand']
            if playercrib:
                comb['weighted'] -= comb['avgCrib']
            else:
                comb['weighted'] += comb['avgCrib']
            combinations.append(comb)
            if comb['weighted'] > maxComb['weighted']:
                maxComb = comb
        return maxComb['cards']

    @staticmethod
    def getPlayCard(hand, playedCards):
        count = 0
        for card in playedCards:
            count+=card.rankInt
        playableCards = [c for c in hand.cards if c.rankInt + count < 32]
        if not playableCards:
            return None
        maxPlay = None
        maxPts  = 0
        for c in playableCards:
            pts = PeggingCounter.score(playedCards, c)
            if pts > maxPlay:
                maxPlay = c
                maxPts = pts
        if maxPlay:
            return maxPlay
        # Try to set up a three-of-a-kind (look for pair in hand)
        for c in cards[:-1]:
            if c.rankInt == cards[-1].rankInt:
                return c
        # Try to set up a run
        # Doesn't matter what order cards are played, but prefer to have two
        # Cards with rank difference == 1 since then odds of a run are double
        for c1 in cards:
            for c2 in cards if c2 != c1:
                if abs(c1.rankInt - c2.rankInt == 1):
                    return c1
        for c1 in cards:
            for c2 in cards if c2 != c1:
                if abs(c1.rankInt - c2.rankInt == 2):
                    return c1
        # Play the highest card!!
        maxCard = cards[0]
        for c in cards[1:]:
            if c.rankInt > maxCard.rankInt:
                maxCard = c
        return maxCard
