'''
Name: Jarron Bailey
Homework 3
Date: 02/11/2019
'''

# Get size of credit card number


def getSize(number):
    return len(number)

# Returns an array of valid numbers


def cardNumberParser():
    card_number = input("Enter your credit card number: ")
    # Check card number length and if it consits of all numbers
    if (getSize(card_number) >= 13 and getSize(card_number) <= 16) and card_number.isdigit():
        return card_number
    else:
        return print("\nPlease Enter a valid credit card number!")

# If number has one digit return number as integer
# If number has two digits return sum of both digits


def getDigit(number):
    if len(number) >= 2:
        sum = 0
        for num in number:
            num = int(num)
            sum += num
        return sum
    else:
        number = int(number)
        return number

# Returns sum of every other number doubled and added to together starting at index 0


def sumOfDoubleEvenPlace(card_number):
    numbersSumArray = []
    numbers = []
    sumOfNumbers = 0

    # For every other index starting at 0
    for idx, char in enumerate(card_number):
        if idx % 2 == 0:
            char = int(char)
            numbers.append(char)
        else:
            continue
    # Loop through each number in the array and double it
    for num in numbers:
        numDoubled = num * 2

        # Convert the product in to a string
        numDoubledString = str(numDoubled)

        # return single digit or sum of multiple digits
        numDoubled = getDigit(numDoubledString)

        numbersSumArray.append(numDoubled)
    for num in numbersSumArray:
        sumOfNumbers += num
    return sumOfNumbers


# Return sum of odd places numbers
def sumOfOddPlace(numbers):
    numsInOddIndex = []
    sumOfNumbers = 0
    for idx, char in enumerate(numbers):
        # For every odd indexed number
        if idx % 2 == 1:
            char = int(char)
            numsInOddIndex.append(char)
        else:
            continue
    numsInOddIndex.reverse()

    # Add the sum
    for num in numsInOddIndex:
        sumOfNumbers += num
    return sumOfNumbers

# Return sum of even positioned number and odd positioned numbers


def sumEvenAndOddPlaces(even, odd):
    return even + odd


# Returns true if credit card is valid or not
def isValid(number):
    valid = False
    if number % 10 == 0:
        valid = True
    return valid


def prefixedMatched(number, prefix):
    startWith = False
    number = str(number)
    startWith = number.startswith(prefix)
    return startWith

# Return the first digit up to end position
# If end position is grater than the number return the number


def getPrefix(number, endPos):
    number = str(number)
    prefix = str(endPos)
    numString = ""
    if prefix < number:
        numString = number[0:endPos]
        return int(numString)
    else:
        return int(number)

# Determine the card type


def determineCardType(card_number):
    card_type = ""
    if prefixedMatched(card_number, "4"):
        card_type = "Visa"
    elif prefixedMatched(card_number, "5"):
        card_type = "MasterCard"
    elif prefixedMatched(card_number, "37"):
        card_type = "American Express"
    elif prefixedMatched(card_number, "6"):
        card_type = "Discover"
    return card_type

# Determine how many digits in the prefix


def getPrefixCount(prefix):
    prefix = str(prefix)
    prefixLength = len(prefix)
    prefixLength = int(prefixLength)
    return prefixLength


card_number = cardNumberParser()
prefix = input("Enter card prefix: ")
print("Does the card number contains prefix: ",
      prefixedMatched(card_number, prefix))
# Feed get count of the prefix into the getPrefix func
print("The prefix of card number is:", getPrefix(
    card_number, getPrefixCount(prefix)))

evensSum = sumOfDoubleEvenPlace(card_number)
oddsSum = sumOfOddPlace(card_number)
sumOfEvenAndodd = sumEvenAndOddPlaces(evensSum, oddsSum)
print("Is this card number valid:", isValid(sumOfEvenAndodd))

# 4388576018402626
# 4388576018410707
