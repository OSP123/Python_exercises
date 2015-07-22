""" Reads a number from the user and prints "zero", "negative" or "positive"
    depending on the number's value.
"""

userInput = input("Please type a number: ") # prompt and read
if userInput.isnumeric():
    userInput = int (userInput)                # convert from string to int
    if userInput > 0:
        print ("positive")
    elif userInput < 0:
        print ("negative")
    else:
        print ("zero")
else:
    print ("Dude, use a number");


