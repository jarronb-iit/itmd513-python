'''
Jarron Bailey
Homework 12
Date: April 29nd, 2019
Description: This program illustrates recursion by reversing numbers and return the number as an hexadecimal number
'''


def convertNumbers(numArray, reversedNumArray=[], hexAccumulator=[]):
    '''
    Function to Recursively finds and returns a number hexadecimal value
    0=0, 1=1, 2=2, 3=3, 4=4, 5=5, 6=6, 7=7, 8=8, 9=9, 10=,A, 11=B, 12=C, 13=D, 14, E, 15=F
    '''
    index = len(numArray)
    index -= 1
    num = numArray.pop()
    reversedNumArray.append(num)
    hexAccumulator.append(hex(num)[2:])
    if len(numArray) > 0:
        convertNumbers(numArray, reversedNumArray, hexAccumulator)
    else:
        def printFunction():
            print("Reversed Numbers: ", ", ".join(str(x)
                                                  for x in reversedNumArray))
            print("Hexadecimal values: ", ", ".join(hexAccumulator))
        return printFunction()


def vaildateInt(number):
    '''Function validates an integer passed in as an string or number and returns valid or not and the number'''
    valid = False
    number.strip()
    if isinstance(number, str):
        try:
            number = int(number)
        except ValueError:
            valid = False
    if isinstance(number, int):
        valid = True

    return {"valid": valid, "number": number}


def main():
    '''
    Main function gets inputs from user, validates it, and passes the input to the number conversion function
    '''

    # Initializing
    valid = False
    print("")
    print("Program will reverse the order the number list entered and translate each number to a hexadecimal.")
    print("Please enter number separated by a comma.")
    print("")
    numArray = input("Number list: ")
    numArray = numArray.split(",")
    integerArray = []

    # Validating Input
    for num in numArray:
        validationVars = vaildateInt(num)
        valid = validationVars["valid"]
        integerArray.append(validationVars["number"])
        if not valid:
            break

    # While not valid get user input
    while not valid:
        print("")
        numArray = input("Number list invalid, please try again\nNumberList: ")
        numArray = numArray.split(",")
        integerArray = []
        for num in numArray:
            validationVars = vaildateInt(num)
            valid = validationVars["valid"]
            integerArray.append(validationVars["number"])
            if not valid:
                break

    # If valid convert numbers
    if valid:
        convertNumbers(integerArray)


# Run main
main()
