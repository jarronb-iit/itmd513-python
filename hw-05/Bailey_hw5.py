'''
Jarron Bailey
Homework 5
Description: This python file contains two programs, one program returns a sorted list
and the other multiplies two matrixes
'''

import math


def retrieveList():
    '''Takes array form user input and checks to see if its valid'''
    valid = False
    while not valid:
        numList = input("Enter a list of numbers(seperated by space): ")
        numsArray = numList.strip().split(" ")
        valid = isValid(numsArray)
        if len(numList) == 1:
            valid = False
        if not valid:
            print("\n" + "Please enter a valid list of number!")

    # Convert Array to int or float, to be sorted correctly
    for ctr in range(len(numsArray)):
        try:
            num = numsArray[ctr]
            numsArray[ctr] = int(num)
        except:
            num = numsArray[ctr]
            numsArray[ctr] = float(num)

    return numsArray


def isValid(numsArray):
    '''If each row user inputs is valid the return the row'''
    ctr = 0
    valid = False
    validRow = []
    while ctr < len(numsArray):
        num = numType(numsArray[ctr])
        if num == "":
            numsArray.pop(ctr)
        if not isinstance(num, str):
            valid = True
            validRow.append(num)
        else:
            valid = False
            return valid
        ctr += 1
    return validRow


def numType(num):
    '''Takes a number and tries to parses the number into int, float, or string'''
    try:
        if int(num) == float(num):
            num = int(num)
            return num
    except:
        try:
            float(num)
            num = float(num)
            return num
        except:
            return num


# Program 2
def retrieveMatrix(firstRow=True, rowLen=0, firstMatrix=True, matrixLen=0):
    '''Creates a matrix row by row and validates each row'''
    matrix = []
    valid = False
    quit = False
    rowEntered = False
    ctr = 1

    print("Enter a matrix of numbers below, please seperate each number by space.")
    print("Enter `q` to complete matrix.")

    # Continue to input colounms until "q" is entered
    while not quit:
        numList = input("Row: ")
        row = numList.strip().split(" ")
        validRow = isValid(row)
        valid = False

        #  Validation of each row
        if type(validRow) is list:
            valid = True
            row = validRow
        if str(row).lower().strip() == '':
            valid = False
            continue
        if len(row) > 0:
            if str(row[0]).lower() == 'q' and rowEntered:
                row.pop()
                quit = True
                valid = False
                break
        if (not valid) and not quit:
            valid = False
            print("\n" + "Please enter a valid row of numbers!")
        if not firstRow and len(row) != rowLen:
            valid = False
            print("\n" + "Row lengths must be equal to first row!")

        # If Valid then set matrix row length for other rows, and append row to matrix
        if valid:
            matrix.append(row)
            rowEntered = True
            if len(matrix) == matrixLen and firstMatrix == False:
                break
            if firstRow and not quit:
                rowLen = len(row)
                firstRow = False
            if firstMatrix:
                matrixLen = len(matrix)

    return {"matrix": matrix, "rowLen": rowLen, "matrixLen": matrixLen}


def splitArray(resultsArray, rowLen):
    '''Takes an array and return small arrays bases on given row legnth'''
    matrix = []
    row = []
    resultsArray = resultsArray[0]
    lenOfArray = len(resultsArray)

    while lenOfArray > 0:
        filterArray = []
        filterArray = resultsArray[0:rowLen]
        row = filterArray
        matrix.append(row)
        if lenOfArray > 0:
            for x in filterArray:
                resultsArray.remove(x)
            lenOfArray = lenOfArray - rowLen
    return matrix


def multiplyMatrix(matrix1, matrix2):
    '''Multiplies two matrixes and return a result'''
    result = []
    X = matrix1
    Y = matrix2
    rowLen = len(matrix1[0])
    maxtrixLen = len(X)
    results = []
    resultRow = []

    for i in range(maxtrixLen):
       # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            result = 0
            for k in range(len(Y)):
                # results[i][j] += X[i][k] * Y[k][j]
                try:
                    result += X[i][k] * Y[k][j]
                except:
                    pass
                resultRounded = round(result, 2)
            resultRow.append(resultRounded)
    results.append(resultRow)

    a1 = splitArray(results, rowLen)
    return a1


def printResults(matrix1, matrix2, results):
    '''
    Loops through the two matrixes and the result to create a template for printing to console
    Returns an array with strings to be printed
    '''

    symbolsPrinted = False
    middleOfMatrix = math.floor(len(matrix1)/2)

    rowLen = len(matrix1[0])

    writeToConsole = []

    for ctr in range(len(matrix1)):
        row = ""
        for i in range(len(matrix1[ctr])):
            row += str(matrix1[ctr][i]) + " "
            if (ctr == middleOfMatrix and i == rowLen - 1) and not symbolsPrinted:
                row += "*"
            else:
                row += " "
            row += " "
        for i in range(len(matrix2[ctr])):
            row += str(matrix2[ctr][i]) + " "
            if (ctr == middleOfMatrix and i == rowLen - 1) and not symbolsPrinted:
                row += "="
                symbolsPrinted = True
            else:
                row += " "
            row += " "
        for i in range(len(results[ctr])):
            row += str(results[ctr][i]) + " "

        writeToConsole.append(row)

    return writeToConsole


def main():
    #     '''Sorted array'''
    #     numList = retrieveList()
    #     numList.sort()
    #     print(numList)
    #     print("")
    '''Matrix Program'''
    matrixVars = retrieveMatrix()
    print("")
    matrixVars2 = retrieveMatrix(
        False, matrixVars["rowLen"], False, matrixVars["matrixLen"])

    results = multiplyMatrix(matrixVars["matrix"], matrixVars2["matrix"])
    writeToConsole = printResults(
        matrixVars["matrix"], matrixVars2["matrix"], results)

    '''Prints strings from the given arrray to the console'''
    for x in range(len(writeToConsole)):
        print(writeToConsole[x])


main()

# results = multiplyMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9, ]], [
#     [0, 2.0, 4.0], [1, 4.5, 2.2], [1.1, 4.3, 5.2]])
