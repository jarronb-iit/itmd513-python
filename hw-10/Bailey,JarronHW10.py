'''
Jarron Bailey
Homework 10
Date: April 15th, 2019
Description: This program illustrates inheritance by creating a parent Employee class and
creating a subclass called ProductionWorker. The user should be able to enter information
about who they are, employee number, shift number, and hourly pay rate.
'''

import re
import datetime
now = datetime.datetime.now()


class Employee:
    '''Parent class "Employee that contains employee name and number'''

    def __init__(self, employeeName=None, employeeNumber=None):
        '''Constructor initializes employee name and number  '''
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber

    def setEmployeeName(self, employeeName):
        '''Mutator function to set Employee name and capitalize name'''
        nameArray = employeeName.split(" ")
        for name in range(len(nameArray)):
            nameArray[name] = nameArray[name].capitalize()
        employeeName = (" ").join(nameArray)
        self.__employeeName = employeeName
        return print("Employee name set...")

    def setEmployeeNumber(self, employeeNumber):
        '''Mutator function to set Employee number'''
        self.__employeeNumber = employeeNumber
        return print("Employee number set...")

    def getEmployeeName(self):
        '''Accessor function to get Employee name'''
        return self.__employeeName

    def getEmployeeNumber(self):
        '''Accessor function to get Employee number'''
        return self.__employeeNumber

    def vaildateEmployeeName(self, employeeName):
        '''Function to validate if the name contains only letters and a space if more than firstname is given and returns valid or not'''
        valid = False
        if re.match("^[a-zA-Z ]+$", employeeName):
            valid = True
        return valid

    def vaildateInt(self, number):
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

    def vaildateFloat(self, number):
        '''Function validates an float passed in as an string or number and returns valid or not'''
        valid = False
        if isinstance(number, str):
            try:
                number = float(number)
            except ValueError:
                valid = False
        if isinstance(number, float):
            valid = True
        return valid


class ProductionWorker(Employee):
    '''ProductionWorker class has employee shift number and hourly pay rate and
    extends Parent class Employees which has employee name and number'''

    def __init__(self, employeeName=None, employeeNumber=None, shiftNumber=None, hrPayRate=None):
        '''Constructor initializes employee name and number with Parent Class
        and initializes shift number and hourly pay right within ProductionWorker class'''
        super().__init__(employeeName, employeeNumber)
        self.__shiftNumber = shiftNumber
        self.__hrPayRate = hrPayRate

    def setShiftNumber(self, shiftNumber):
        '''Mutator function to set Employee number'''
        self.__shiftNumber = shiftNumber
        return print("Shift number set...")

    def setHrPayRate(self, hrPayRate):
        '''Mutator function to set Employee hourly pay rate'''
        self.__hrPayRate = hrPayRate
        return print("Hourly pay rate set..")

    def getShiftNumber(self):
        '''Accessor function to get Employee shift number'''
        return self.__shiftNumber

    def getHrPayRate(self):
        '''Accessor function to get Employee hourly pay rate'''
        return self.__hrPayRate

    def getEmployeeDetails(self):
        '''
        Function gets Employees name and number from parent class
        and gets the shift number and hourly pay rate from the child class
        '''
        employeeName = super().getEmployeeName()
        employeeNumber = super().getEmployeeNumber()
        shiftNumber = self.getShiftNumber()
        hrPayRate = self.getHrPayRate()

        return {"employeeName": employeeName, "employeeNumber": employeeNumber, "shiftNumber": shiftNumber, "hrPayRate": hrPayRate}

    def setEmployeeDetails(self):
        '''Function gets user inputs, validates it and returns a dictionary of the Employee details: name, number, shift number, and hourly pay rate'''
        isValidName = False
        isValidNumber = False
        isValidShiftNumber = False
        isValidHrPayRate = False

        # Validate Employee name
        while not isValidName:
            employeeName = input("Employee name: ")
            isValidName = super().vaildateEmployeeName(employeeName)
            if isValidName:
                super().setEmployeeName(employeeName)
                isValidName = True
                break
            print("\nPlease enter valid name.\n")

        # Validate Employee number
        while not isValidNumber:
            employeeNumber = input("\nEmployee Number: ")
            isValidNumber = super().vaildateInt(employeeNumber)
            if isValidNumber:
                super().setEmployeeNumber(employeeNumber)
                isValidNumber = True
                break
            print("\nPlease enter valid number.")

        # Validate Employee shift number
        while not isValidShiftNumber:
            shiftNumber = input("\nShift number: ")
            isValidShiftNumber = super().vaildateInt(shiftNumber)
            if isValidShiftNumber:
                if int(shiftNumber) < 1 or int(shiftNumber) > 2:
                    isValidShiftNumber = False
                else:
                    self.setShiftNumber(shiftNumber)
                    isValidShiftNumber = True
                    break
            print("\nPlease enter valid number.")

        # Validate Employee hourly pay rate
        while not isValidHrPayRate:
            hrPayRate = input("\nHourly rate: ")
            isValidHrPayRate = super().vaildateFloat(hrPayRate)
            if isValidHrPayRate:
                self.setHrPayRate(hrPayRate)
                isValidHrPayRate = True
                break
            print("\nPlease enter valid pay rate.")

        return {"employeeName": employeeName, "employeeNumber": employeeNumber, "shiftNumber": shiftNumber, "hrPayRate": hrPayRate}


obj = ProductionWorker()
obj.setEmployeeDetails()
empVars = obj.getEmployeeDetails()

print("")
print("******** Receipt ********")
print("Employee name: {}".format(empVars["employeeName"]))
print("Employee number: {}".format(empVars["employeeNumber"]))
print("Employee shift number: {}".format(empVars["shiftNumber"]))
print("Employee hourly pay rate: {:0.2f}".format(float(empVars["hrPayRate"])))
print("Date: {}".format(now.strftime("%m-%d-%Y")))
print("Time: {}".format(now.strftime("%H:%M")))
