import math


def retrieveList():
    '''Takes array form user inout and checks to see if its valid'''
    valid = False
    while not valid:
        numList = input("Enter a list of numbers(seperated by space): ")
        numsArray = numList.strip().split(" ")
        valid = isValid(numsArray)
        if not valid:
            print("\n" + "Please enter a valid list of number!")
    return numsArray


def isValid(numsArray):
    '''if each row user inputs is valid the return the row'''
    ctr = 0
    valid = False
    validRow = []
    while ctr < len(numsArray):
        num = numType(numsArray[ctr])
        if not isinstance(num, str):
            valid = True
            validRow.append(num)
        elif num == "":
            numsArray.pop(ctr)
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


'''Program Two'''


def retrieveMatrix(firstRow=True, matrixLen=0):
    '''takes martix row by row from user'''
    matrix = []
    valid = False
    quit = False

    print("Enter a matrix of numbers below, please seperate each number by space.")
    print("Enter `q` to complete matrix.")

    '''Continue to input colounms until "q" is entered '''
    while not quit:
        numList = input("Row: ")
        row = numList.strip().split(" ")
        validRow = isValid(row)

        '''Validation of each row'''
        if type(validRow) is list:
            valid = True
            row = validRow
        else:
            valid = False

        if str(row[0]).lower() == 'q':
            quit = True
        elif (not valid) and not quit:
            print("\n" + "Please enter a valid row of numbers!")
        elif not firstRow and len(row) != matrixLen:
            print("\n" + "Row lengths must be equal to first row!")
        else:
            '''If Valis then set matrix row length for other rows, and append row to matrix'''
            if firstRow:
                matrixLen = len(row)
            firstRow = False
            matrix.append(row)
    return {"matrix": matrix, "matrixLen": matrixLen}


def splitArray(resultsArray, rowLen):
    '''Takes an array and return small arrays bases on given row legnth'''
    matrix = []
    resultsArray = resultsArray[0]
    row = []
    lenOfArray = len(resultsArray)

    while lenOfArray > 0:
        filterArray = []
        filterArray = resultsArray[0:rowLen]
        print(filterArray)
        row = filterArray
        matrix.append(row)
        resultsArrayFiltered = resultsArray.remove(filterArray)
        resultsArray = resultsArrayFiltered
        lenOfArray = lenOfArray - rowLen
    return matrix


def multiplyMatrix(matrix1, matrix2):
    '''Muiltple two matrixes and return a result'''
    result = []
    X = matrix1
    Y = matrix2
    rowLen = len(matrix1[0])
    results = []
    resultRow = []

    for i in range(len(X)):
       # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            result = 0
            for k in range(len(Y)):
                # results[i][j] += X[i][k] * Y[k][j]
                result += X[i][k] * Y[k][j]
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
        row += "\t"
        for i in range(len(matrix2[ctr])):
            row += str(matrix2[ctr][i]) + " "
            if (ctr == middleOfMatrix and i == rowLen - 1) and not symbolsPrinted:
                row += "="
                symbolsPrinted = True
        row += "\t"
        for i in range(len(results[ctr])):
            row += str(results[ctr][i]) + " "

        writeToConsole.append(row)

    return writeToConsole


def main():
    '''Sorted array'''
    numList = retrieveList()
    numList.sort()
    print(numList)

    '''Matrix Program'''
    # matrixVars = retrieveMatrix()
    # matrixVars2 = retrieveMatrix(False, matrixVars["matrixLen"])

    # results = multiplyMatrix(matrixVars["matrix"], matrixVars2["matrix"])

    # writeToConsole = printResults(
    #     matrixVars["matrix"], matrixVars2["matrix"], results)

    # '''Prints strings from the given arrray to the console'''
    # for x in range(len(writeToConsole)):
    # print(writeToConsole[x])


main()

results = multiplyMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9, ]], [
    [0, 2.0, 4.0], [1, 4.5, 2.2], [1.1, 4.3, 5.2]])
printResults([[1, 2, 3], [4, 5, 6], [7, 8, 9, ]], [
    [0, 2.0, 4.0], [1, 4.5, 2.2], [1.1, 4.3, 5.2]], results)
writeToConsole = (printResults([[1, 2, 3], [4, 5, 6], [7, 8, 9, ]], [
    [0, 2.0, 4.0], [1, 4.5, 2.2], [1.1, 4.3, 5.2]], results))

'''Prints strings from the given arrray to the console'''
for x in range(len(writeToConsole)):
    print(writeToConsole[x])
