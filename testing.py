"""
Write a function that takes a whole number as parameter and returns a
string containing the number spelled out in English
"""
firstNineteen = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
largerSuffix = ["hundred", "thousand", "million"]

# Prints out the numbers for numbers < 1000
def smallNumToWords(num):
    numList = [int(i) for i in str(num)]
    
    if num < 0:
        print("minus")
        num *= -1

    if 0 <= num <= 19:
        return firstNineteen[num]
    elif 20 <= num <= 99:
        if numList[-1] == 0:
            return tens[numList[0]]
        else:
            return tens[numList[0]] + " " + firstNineteen[numList[1]]
    elif 100 <= num <= 999:
        if num % 100 == 0:
            return firstNineteen[numList[0]] + " hundred"
        else:
            return firstNineteen[numList[0]] + " hundred and " + tens[numList[1]] + "-" + firstNineteen[numList[2]]

def largeNumToWords(num):

def decrease(num):
    if num % 1000 == 0:
        return num       # this is called the trivial case
    elif num > 1:
        return number * factorial (number -1)  # here is the recursive call
    else:
        return 1       

print (factorial (5))



print(smallNumToWords(34))
print(smallNumToWords(145))

    
    
