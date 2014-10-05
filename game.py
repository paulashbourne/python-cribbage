from deck import Deck
from hand import Hand
from peggingCounter import PeggingCounter

class Game():

    WINPTS = 121

    def __init__(self):
        self.playerPoints = 0
        self.computerPoints = 0

    def awardPoints(player, value):
        if player:
            self.playerPoints += value
        else:
            self.computerPoints += value

class Round():

    def __init__(self, game, playerDeals):
        self.playerDeals = playerDeals
        self.deck = Deck()
        self.playerHand = Hand()
        self.computerHand = Hand()
        self.crib = Hand(True)
        self.playedCardsPlayer = []
        self.playedCardsComputer = []
        self.cardsInPlay = []

    def deal(self):
        this.deck.reset()
        this.deck.shuffle()
        for x in range(6):
            this.playerHand.append(deck.pop())
            this.computerHand.append(deck.pop())
        this.playerHand.sort()
        this.computerHand.sort()

    def playhand(self):
        crib = Hand(True)

        # Computer deposit cards to crib
        self.depositToCrib(computerHand,
                AI.getDepositCards(computerHand, playerDeals))

        # Player deposit cards to crib
        self.depositToCrib(playerHand,
                Player.getDepositCards(playerHand, playerDeals))

        getUpcard()

        while len(playerHand) + len(computerHand) > 0:
            if playerTurn:
                self.playerHand. 
    
    def depositToCrib(hand, cards):
        for c in cards:
            self.crib.append(c)
            hand.remove(c)

    def getUpcard(self):
        upcard = self.deck.pop()
        if upcard.rankInt == 10:
            self.game.awardPoints(self.playerdeals, 2)
        if self.game.playerPoints >= 121 or self.game.computerPoints >= 121:
            self.game.gameover()
            return

    def playCard(self, card):
        count = 0
        for c in self.cardsInPlay:
            count += c.rankInt
        count += card.rankInt
        if count > 31:
            return False
