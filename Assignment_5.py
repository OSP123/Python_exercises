"""
Card class that contains a constructor, stringifier, accessors for members,
and a method for returning the blackjack value of a Card. Card contains 2
members (taken in through constructor): rank and suit. Rank is an integer
between 1-13 that represents value of card (Ace, 10, etc.) and suit represents
the suit of the card. Testing is performed at the end. 
"""
"""
Card object represents an instance of a Card class, containing the rank and
suit of the card.
"""
class Card:    
    """ constructor that sets the values for rank and suit when Card is
        instantiated. If bad values are sent, default values take their place.       
    """
    def __init__(self, rank, suit):
        if rank >= 1 and rank <= 13:
            self.rank = rank
        else:
            self.rank = 1
        if suit == "d" or suit == "c" or suit == "h" or suit == "s":
            self.suit = suit
        else:
            self.suit = "d"
    #returns a string of the calling card instance's rank and suit.
    def __str__(self):
        faceList = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        face = ""
        suitMask = ""
        if self.suit == "c":
            suitMask += "Clubs"
        elif self.suit == "h":
            suitMask += "Hearts"
        elif self.suit == "s":
            suitMask += "Spades"
        elif self.suit == "d":
            suitMask += "Diamonds"
        face += faceList[self.rank]
        return "%s of %s" % (face, suitMask)
    
    #returns the rank of the calling card instance
    def getRank(self):
        return self.rank
    
    #returns the suit of the calling card instance
    def getSuit(self):
        return self.suit
    
    #returns a blackjack value based on rank of the calling card instance
    def bjValue(self):
        if self.rank >= 10 and self.rank <= 13:
            return 10
        else:
            return self.rank

#Testing 5 different cards, their output, and the blackjack value of a card
if __name__ == "__main__":
    card1 = Card(3,"s")
    print (card1)
    print (card1)
    card2 = Card(5,"c")
    print (card2)
    card3 = Card(11,"c")
    print (card3.bjValue())
    print (card3)
    card4 = Card(13, "h")
    print (card4)
    card5 = Card(1, "d")
    print (card5)
"""----------------------------------------Output-------------------------------
Three of Spades
Three of Spades
Five of Clubs
10
Jack of Clubs
King of Hearts
Ace of Diamonds
--------------------------------------------------------------------------------
"""
