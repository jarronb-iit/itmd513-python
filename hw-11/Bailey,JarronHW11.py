'''
Jarron Bailey
Homework 11
Date: April 22nd, 2019
Description: This program illustrates polymorphism by using a base Ship class
and instantiating to different variations of it and adding features prospectively
to a CruiseShip and a CargoShip
'''
import re


class Ship:
    '''
    This is the base class Ship which has two attributes name and year 
    '''

    def __init__(self, nameOfShip=None, shipYear=None):
        '''Constructor initializes name of ship, ship year and errors variable'''
        self.__nameOfShip = nameOfShip
        self.__shipYear = shipYear
        self.error = False

    def setNameOfShip(self, nameOfShip):
        '''Mutator method for ships name if valid'''
        valid = self.vaildateShipName(nameOfShip)
        if not valid:
            self.error = True
            print(" Ship name not set, Please enter valid name")
            return
        self.__nameOfShip = nameOfShip
        return print("Ship name set...")

    def setYearOfShip(self, shipYear):
        '''Mutator method for ships year if valid'''
        valid = self.vaildateInt(shipYear)
        if not valid:
            self.error = True
            print("Ship year not set, Please enter valid year")
            return
        self.__shipYear = shipYear
        return print("Ship years set...")

    def getNameOfShip(self):
        '''Accessor method to get ships name '''
        return self.__nameOfShip

    def getShipYear(self):
        '''Accessor method to get ships year'''
        return self.__shipYear

    def vaildateShipName(self, shipName):
        '''
        Method to validate if the ships name has all letters
        return if its valid
        '''
        valid = False
        if re.match("^[a-zA-Z ]+$", shipName):
            valid = True
        return valid

    def vaildateInt(self, number):
        '''
        Method to validate if the ships year is an integer
        return if its valid
        '''
        '''Function validates an integer passed in as an string or number and returns valid or not'''
        valid = False
        if isinstance(number, str):
            try:
                number = int(number)
            except ValueError:
                valid = False
        if isinstance(number, int):
            valid = True
        return valid

    def getShipInformation(self):
        '''Method that returns the ships name and year '''
        if self.error:
            return print("Fix errors and try again")
        return print("Name of ship: {}\nShip built in year: {}".format(self.__nameOfShip, self.__shipYear))


class CruiseShip(Ship):
    '''Class derived from the base class Ship, adds a max capacity attribute'''

    def __init__(self, nameOfShip=None, shipYear=None, maxCapacity=None):
        '''Constructor initializes name, year, and max capacity'''
        super().__init__(nameOfShip, shipYear)
        self.__maxCapacity = maxCapacity

    def setMaxCapacity(self, maxCapacity):
        '''Mutator method to set cruise ships max capacity if valid'''
        valid = super().vaildateInt(maxCapacity)
        if not valid:
            self.error = True
            print("Ships max capacity not set, Please enter valid capacity")
            return
        self.__maxCapacity = maxCapacity
        return print("Cruise ship's max capacity of people set")

    def getMaxCapacity(self):
        '''Accessor method to get cruise ships max capacity '''
        return self.__maxCapacity

    def getShipInformation(self):
        '''Method to retrieve cruise ships name and max capacity'''
        if self.error:
            return print("Fix errors and try again")
        return print("Name of ship: {}\nShip's capacity: {} people".format(self.getNameOfShip(), self.__maxCapacity))


class CargoShip(Ship):
    '''Class derived from the base class Ship, adds a max capacity attribute'''

    def __init__(self, nameOfShip=None, shipYear=None, maxCapacity=None):
        '''Constructor initializes name, year, and max capacity'''
        super().__init__(nameOfShip, shipYear)
        self.__maxCapacity = maxCapacity

    def setMaxCapacity(self, maxCapacity):
        '''Mutator method to set cruise ships max capacity if valid'''
        valid = super().vaildateInt(maxCapacity)
        if not valid:
            self.error = True
            print("Ships max capacity not set, Please enter valid capacity")
            return
        self.__maxCapacity = maxCapacity
        return print("Cargo ship's max tonnage capacity set")

    def getMaxCapacity(self):
        '''Accessor method to get cargo ships max capacity '''
        return self.__maxCapacity

    def getShipInformation(self):
        '''Method to retrieve cargo ships name and max capacity'''
        if self.error:
            return print("Fix errors and try again")
        return print("Name of ship: {}\nShip capacity: {} tons".format(self.getNameOfShip(), self.__maxCapacity))


def main():
    '''Main method to run program'''
    def printShipinformation(ship):
        '''Helper function to check instance of class and set correct properties prospectively'''

        # Cargo Ship
        if isinstance(ship, CargoShip):
            print("")
            print("Cargo ship")
            print("********************************")
            ship.setNameOfShip("Cargo ship")
            ship.setMaxCapacity(40000)
            print("")
            ship.getShipInformation()
            print("")
            print("********************************")
            print("")

        # Cruise Ship
        elif isinstance(ship, CruiseShip):
            print("")
            print("Cruise ship")
            print("********************************")
            ship.setNameOfShip("Cruise ship")
            ship.setMaxCapacity(15000)
            print("")
            ship.getShipInformation()
            print("")
            print("********************************")
            print("")

        # Regular Ship
        elif not isinstance(ship, CruiseShip) and not isinstance(ship, CargoShip):
            print("")
            print("Regular ship")
            print("********************************")
            ship.setNameOfShip("Regular ship")
            ship.setYearOfShip(1829)
            print("")
            ship.getShipInformation()
            print("")
            print("********************************")
            print("")

    # Instantiate classes
    regShip = Ship()
    cargoShip = CargoShip()
    cruiseShip = CruiseShip()

    # Create array of class objects
    listOfShips = [regShip, cargoShip, cruiseShip]

    # Loop through each object and call helper function, which check class and set attributes
    for ship in listOfShips:
        printShipinformation(ship)


main()
