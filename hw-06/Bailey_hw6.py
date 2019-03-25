'''
Jarron Bailey
Homework 6
Description: This python file outputs an expenses pie chart bases on a "expenses.txt" file
and also creates an line graph of 1996 weekly gas averages based on "1994_Weekly_Gas_Averages.txt" file
'''

import matplotlib.pyplot as plt
import sys


def getExpenses():
    '''Reads the "expenses.txt" file and returns an dictionary of expenses'''

    try:
        fileName = "expenses.txt"
        f = open(fileName, 'r')
    except FileNotFoundError:
        print('There was an error opening the file "{}"!'.format(fileName))
        print("Please check file name.")
        sys.exit()

    expenses = f.readlines()
    expensesList = {}

    # Iterate through expenses remove the EOL symbol
    # and split the expense name and prince into a
    # dictionary entry

    try:
        for expense in expenses:
            expense = expense.replace("\n", "")
            expense = expense.replace("-", " ")
            expense = expense.split("=")
            expenseName = expense[0].capitalize().strip()
            expenseAmount = expense[1].strip()
            expensesList[expenseName] = expenseAmount
    except IndexError:
        print('There was an error parsing the "{}" file!'.format(fileName))
        print("Each expense should be on a separate line in the format, expense=amount")
        sys.exit()
    f.close()
    return expensesList


def createExpensePieChart(expenses):
    '''
    Creates an pie chart from expenses and saves it into
    the "expenses-pie-chart.pdf" file
    '''

    fileName = "expenses-pie-chart.pdf"
    expensesNames = list(expenses.keys())
    expensesAmounts = list(expenses.values())
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = expensesNames
    sizes = expensesAmounts

    # only "explode" the 1st slice which is also the largest amount
    explode = (0.1, 0, 0, 0, 0, 0)
    plt.rcParams["figure.figsize"] = (10, 10)
    plt.rcParams['font.size'] = 9.0
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
           shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')
    plt.title("Jarron's Expenses", bbox={'facecolor': '0.8', 'pad': 5})

    try:
        plt.savefig(fileName)
        plt.close()
    except OSError:
        print('There was an error export the file "{}"!'.format(fileName))
        print("Please make sure the file is closed.")


def getWeeklyGasAvgs():
    '''
    Reads the "1994_Weekly_Gas_Averages.txt" file
    and returns a list of gas prices
    '''

    try:
        fileName = "1994_Weekly_Gas_Averages.txt"
        f = open(fileName, 'r')
    except FileNotFoundError:
        print('There was an error opening the file "{}"!'.format(fileName))
        print("Please check file name.")
        sys.exit()
    formattedAvgs = []
    weeklyGasAvgs = f.readlines()

    for weeklyGasAvg in weeklyGasAvgs:
        weeklyGasAvg = weeklyGasAvg.replace("\n", "")
        formattedAvgs.append(weeklyGasAvg)

    return formattedAvgs


def getAmountOfWeeks(weeksList):
    '''
    Takes in weekly list and counts the amount prices in the
    list to return amount of weeks
    '''
    amountOfWeeks = []
    for weeklyAvg in range(len(weeksList) + 1):
        amountOfWeeks.append(weeklyAvg)
    amountOfWeeks.pop(0)

    return amountOfWeeks


def createGasLineGraph(gasPrices, amountOfWeeks):
    '''
    Creates an line graph and saves it into "gas-line-graph.pdf" file 
    from the gas price list and the amount of weeks
    '''
    fileName = "gas-line-graph.pdf"
    prices = gasPrices
    amountOfWeeks = amountOfWeeks
    plt.rcParams["figure.figsize"] = (10, 10)
    plt.plot(amountOfWeeks, prices, color="blue")
    plt.xlabel('Weeks')
    plt.ylabel('Gas Prices in Dollars')
    plt.title('1994 Weekly Gas Averages', bbox={'facecolor': '0.8', 'pad': 5})

    try:
        plt.savefig(fileName)
        plt.close()
    except OSError:
        print('There was an error export the file "{}"!'.format(fileName))
        print("Please make sure the file is closed.")


def main():
    '''
    Runs functions to create a pie chart for expenses
    and to create a line graph for the 1994 weekly gas prices
    '''
    expenses = getExpenses()
    createExpensePieChart(expenses)
    weeklyGasAvgs = getWeeklyGasAvgs()
    amountOfWeeks = getAmountOfWeeks(weeklyGasAvgs)
    createGasLineGraph(weeklyGasAvgs, amountOfWeeks)


'''Run main'''
main()
