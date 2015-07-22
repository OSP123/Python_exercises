"""
Card class that contains a constructor, stringifier, accessors for members,
and a method for returning the blackjack value of a Card. Card contains 2
members (taken in through constructor): rank and suit. Rank is an integer
between 1-13 that represents value of card (Ace, 10, etc.) and suit represents
the suit of the card. Testing is performed at the end.

This program also adds in some exceptions for wrong type and out of range values
for the rank and suit members of Card class in the __init__ constructor.
"""
"""
Card object represents an instance of a Card class, containing the rank and
suit of the card.
"""
class Card:    
    """ constructor that sets the values for rank and suit when Card is
        instantiated. If bad values are sent, default values take their place.
        Exception testing for wrong type and out of range values for the rank
        and suit members of Card class in the __init__ constructor.
    """
    def __init__(self, rank, suit):
        if type(rank) != int or type(suit) != str:
            raise TypeError()
        if suit in ["d","c","h","s"]:
            self.suit = suit
        else:
            raise ValueError()
        if rank >= 1 and rank <= 13:
            self.rank = rank
        else:
            raise ValueError()

    #returns a string of the calling card instance's rank and suit.
    def __str__(self):
        faceList = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        suitDict = {"c" : "Clubs", "h" : "Hearts", "s" : "Spades", "d" : "Diamonds"}
        face = ""
        suitMask = ""
        suitMask += suitDict[self.suit]
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
    #bad rank argument (wrong type)
    try:
        card1 = Card("hi","s")
    except ValueError:
        print ("rank must be between 1-13 and suit must be h,c,d, or s")
    except TypeError:
        print ("rank must be a string and suit must be an integer")
    #bad suit argument (wrong type)
    try:
        card1 = Card(3,4)
    except ValueError:
        print ("rank must be between 1-13 and suit must be h,c,d, or s")
    except TypeError:
        print ("rank must be a string and suit must be an integer")
    #bad rank argument (out of range rank)
    try:
        card1 = Card(14,"s")
    except ValueError:
        print ("rank must be between 1-13 and suit must be h,c,d, or s")
    except TypeError:
        print ("rank must be a string and suit must be an integer")
    #bad suit argument (not h,c,d, or s)
    try:
        card1 = Card(7,"q")
    except ValueError:
        print ("rank must be between 1-13 and suit must be h,c,d, or s")
    except TypeError:
        print ("rank must be a string and suit must be an integer")
    #good arguments
    try:
        card1 = Card(7,"c")
    except ValueError:
        print ("rank must be between 1-13 and suit must be h,c,d, or s")
    except TypeError:
        print ("rank must be a string and suit must be an integer")
    print (card1)
    print (card1)
    print(card1.getRank())
    print(card1.getSuit())
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
