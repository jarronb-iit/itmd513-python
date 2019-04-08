'''
Jarron Bailey
Homework 9
Date: April 8th, 2019
Description: This program illustrates the use of classes by building a coffee
vending machine application. This class will be instantiated from another file.
'''


class VendingMachine:
    '''
    This class is responsible for providing an api for the building maching
    '''

    def __init__(self, stock, price):
        '''
        Constructor takes stock and price and return a menu if inputs are valid
        '''
        self.__coffeeCupsAvailable = stock
        self.__price = price
        self.__validInteger = True
        self.__validPrice = True
        self.__quarters = 0
        self.__dimes = 0
        self.__nickels = 0
        self.__error = False

        # Validate stock and price
        self.__validInteger = self.__validateInteger(
            self.__coffeeCupsAvailable, "Stock")
        self.__validPrice = self.__validatePrice(self.__price)

        if self.__validInteger and self.__validPrice:
            round(self.__price, 2)
            self.displayMenu()  # Print menu

    def displayMenu(self):
        '''
        Function displays a menu with a title, machine stock, and price per cup.
        '''
        print("========================================================")
        print("{{Coffee Vending Machine}}")
        print("")
        print("Coffee stock: {}".format(self.__coffeeCupsAvailable))
        print("Coffee price: ${:0.2f}".format(self.__price))
        print("")
        print("Insert ${:0.2f} to buy a cup of coffee :)".format(
            self.__price))
        print("========================================================")
        print("")

    def __validateInteger(self, num, item=""):
        '''
        Function determines if the integer entered is valid: an integer and 0 or greater.
        '''
        valid = True
        try:
            num = int(num)
        except ValueError:
            valid = False
            if item == "Stock":
                print("Error: {} entered isn't an integer, Please reenter.".format(item))
        else:
            if num < 0:
                valid = False
                if item == "Stock":
                    print("Error: {} should be 0 or greater.".format(item))
        return valid

    def __validatePrice(self, price):
        '''
        Function determines if the price entered is valid: an number and greater than 0
        '''
        valid = True
        try:
            price = float(price)
        except ValueError:
            valid = False
            print("Error: Price entered isn't an number, Please reenter.")
        else:
            if price <= 0:
                valid = False
                print("Error: Price should be greater than 0.")
        return valid

    def insert(self, quarters, dimes, nickels):
        '''
        Function takes amount quarters, dimes, nickels; validates each amount coins
        and set the coins amount to class values

        '''
        def setCoins(quarters, dimes, nickels):
            '''
            Function to set the amount of quarters, dimes, and nickels to the class
            '''
            self.__quarters = quarters
            self.__dimes = dimes
            self.__nickels = nickels

        # Validate amount of coins
        inValid = []
        validQuarters = self.__validateInteger(quarters)
        if not validQuarters:
            inValid.append("Quarters")

        validDimes = self.__validateInteger(dimes)
        if not validDimes:
            inValid.append("Dimes")

        valideNickels = self.__validateInteger(nickels)
        if not valideNickels:
            inValid.append("Nickels")

        if not validQuarters or not validDimes or not valideNickels:
            self.__error = True
            return print("\n" + ", ".join(inValid) +
                         " must be an integer greater than or equal to 0.")
        return setCoins(quarters, dimes, nickels)

    def __calculateTotalEntered(self):
        '''
        Function calculates the amount total entered amount and returns the sum
        '''
        quarters = float(self.__quarters) * .25
        dimes = float(self.__dimes) * .10
        nickels = float(self.__nickels) * .05

        sum = quarters + dimes + nickels
        return sum

    def refund(self):
        amountEntered = self.__calculateTotalEntered()
        '''Function returns the refund or the change if any'''
        return print("\nMoney returned: ${:0.2f}".format(amountEntered))

    def select(self):
        '''
        Function returns an coffee and change in there are in stock and enough money had been entered.
        If not the function returns an message about the inconvenience.
        '''

        # If error inserting coins , return
        if self.__error:
            return print("\nError: Please try again.")

        amountEntered = self.__calculateTotalEntered()

        if amountEntered < self.__price:
            return print("Not enough money, here's your refund. Try again.")
        if self.__coffeeCupsAvailable == 0:
            return print("Sorry for the inconvenience, there isn't any coffee available please try again later.")

        else:  # If stock and enough money
            change = amountEntered - self.__price
            if change <= 0:
                return print("\nThank you, Please take your cup of coffee.")
            else:
                print("\nSorry this machine takes exact change, Try again.")
                return self.refund()
