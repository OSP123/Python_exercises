from Card import Card
import random

class Hand:    
    """
    Hand object represents a Hand of Card objects, containing randomly generated
    cards upon instantiation, a blackjack value method for all of the cards
    in the hand combined, and a hitMe() method that adds a randomly generated
    card to the Hand. 
    """
    def __init__(self, numCardsInHand):
        """Creates a Hand object with an array of randomly generated Card objects
        whose quantity is set by the client via the argument passed to the init.
        """
        if type(numCardsInHand) == int and numCardsInHand > 0:
            self.numCardsInHand = numCardsInHand
        else:
            raise ValueError()
        self.suitArray = ["d","c","h","s"]
        self.myCards = []
        for i in range(numCardsInHand):
            rankRandom = int(random.uniform(1, 13))
            suitRandom = int(random.uniform(0, 3))
            c = Card(rankRandom, self.suitArray[suitRandom])
            self.myCards.append(c)
    
    def bjValue(self):
        #returns a blackjack value for the whole hand of cards
        bjVal = 0;
        for i in self.myCards:
            if i.rank >= 10 and i.rank <= 13:
                bjVal += 10
            else:
                bjVal += i.rank
        return bjVal
    
    def __str__(self):
    #returns a string of Card Objects in the Hand
        s= ", ".join( [ str(element) for element in self.myCards ] )
        return 'Cards in hand: %s '%( s )
    
    def hitMe(self):
    #adds a randomly generated card to the Hand object
        for i in range(1):
            rankRandom = int(random.uniform(1, 13))
            suitRandom = int(random.uniform(0, 3))
            c = Card(rankRandom, self.suitArray[suitRandom])
            self.myCards.append(c)
