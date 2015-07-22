userInput = input ("Please type a real number: ")

if __name__ == "__main__":
    try:
        float(userInput)
    except ValueError:
        print ("You typed a char that isn't appropriate in a real number.")
    else:
        print ("Thank you for following instructions.")
    finally:
        print ("I hope you play again.")
