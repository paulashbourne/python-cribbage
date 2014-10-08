from card import card
from hand import hand
from copy import copy
from peggingCounter import PeggingCounter

class AI():

    @staticmethod
    def getDepositCards(hand, playercrib):
        cribowner = "your" if playercrib else "the computer's"
        print "Please choose cards to deposit to %s crib. Enter " \
                "the indices of the two cards, separated by a comma."
        print "Your score:"

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

