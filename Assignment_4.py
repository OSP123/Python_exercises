"""
Program has 3 arrays of words depicting the numbers. The function for the small words is used for words < 1000 in length.
The largeNumToWords prints out the numbers that are larger tahn 1000 in length. The output is shown at the bottom.
"""
firstNineteen = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
largerSuffix = ["hundred", "thousand", "million"]

# Prints out the numbers for numbers < 1000
def smallNumToWords(num):
    if num < 0:
        num = negativeToPositive(num)
        
    numList = [int(i) for i in str(num)]

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

# Converts negative number to positive and then returns that number
def negativeToPositive(num):
    print("Minus")
    num = int(num * -1)
    return num

# Splits the larger numbers into smaller, 3 digit integers and puts them into an array
def splitNumbers(num):
    remArray = []
    while num != 0:
        remArray.append(num % 1000)
        num = int(num / 1000)
    return remArray

# Prints out the numbers for numbers > 1000
def largeNumToWords(num):
    if num < 0:
        num = negativeToPositive(num)
    numList = [int(i) for i in str(num)]
    splitArray = splitNumbers(num)
    
    if 1000 <= num <= 999999:
        thousand = smallNumToWords(splitArray[1]) + " thousand "
        if num % 1000 == 0:
            return thousand
        else:
            return thousand + smallNumToWords(splitArray[0])
    elif 100000 <= num <= 999999999:
        million = smallNumToWords(splitArray[2]) + " million "
        if num % 100000 == 0:
            return million
        else:
            return million + smallNumToWords(splitArray[1]) + " thousand " + smallNumToWords(splitArray[0])

print(smallNumToWords(34))
print(smallNumToWords(145))
print(largeNumToWords(100000))
print(largeNumToWords(10000))
print(largeNumToWords(123456))
print(largeNumToWords(123452342))
print(largeNumToWords(100000000))
print(negativeToPositive(-345))
print(largeNumToWords(-123456))
print(largeNumToWords(-123452342))
print(largeNumToWords(-100000000))

""" OUTPUT
thirty four
one hundred and forty-five
one hundred thousand 
ten thousand 
one hundred and twenty-three thousand four hundred and fifty-six
one hundred and twenty-three million four hundred and fifty-two thousand three hundred and forty-two
one hundred million 
Minus
345
Minus
one hundred and twenty-three thousand four hundred and fifty-six
Minus
one hundred and twenty-three million four hundred and fifty-two thousand three hundred and forty-two
Minus
one hundred million
"""
    
