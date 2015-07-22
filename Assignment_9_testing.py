from Card import Card
from Hand import Hand
import random


#Testing different initial values, their output, blackjack values of hand, and hitMe() method.
if __name__ == "__main__":
    
    someHand = Hand(3)
    print(someHand)

    someHand = Hand(2)
    print(someHand)

    someHand = Hand(5)
    print(someHand)
    
    print(someHand.bjValue())
    print(someHand)
    
    someHand.hitMe()
    print(someHand)

"""----------------------------------------Output-------------------------------
Cards in hand: Seven of Hearts, Jack of Hearts, Jack of Clubs 
Cards in hand: Jack of Hearts, Two of Hearts 
Cards in hand: Six of Hearts, Jack of Hearts, Six of Hearts, Four of Diamonds, Five of Diamonds 
31
Cards in hand: Six of Hearts, Jack of Hearts, Six of Hearts, Four of Diamonds, Five of Diamonds 
Cards in hand: Six of Hearts, Jack of Hearts, Six of Hearts, Four of Diamonds, Five of Diamonds, Ace of Clubs 
--------------------------------------------------------------------------------
"""
