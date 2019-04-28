'''
Jarron Bailey
Homework 11
Date: May 6th, 2019
Description: This program is to present a GUI that computes a patient’s bill for a hospital stay.
A GUI that allows the user to enter a type of surgery and a type of medication, and check the patient 
out of the hospital. When the patient checks out, the total charges should be displayed in a Window 
format (GUI Interface).
'''
import re


class PatientAccount:
    '''
    Class is responsible for handling the patients account information - person information,
    and charges accrued for the hospital stay 
    '''

    def __init__(self):
        '''
        Constructor initializes patient's name, patient's date of birth, hospitals daily rate, days in hospital, and the charges accumulated dictionary
        '''

        self.__patientName = None
        self.__patientDateOfBirth = None
        self.__dailyRate = 1878.67
        self.__daysInHospital = 0
        self.__chargesAccumulator = {}

    def getPatientName(self):
        '''Accessor function to return the hospitals patient name'''
        return self.__patientName

    def setPatientName(self, patientName):
        '''Mutator function to set the hospitals patient name'''
        self.__patientName = patientName
        print("Patient name set...")
        return "Patient name set..."

    def getPatientDateOfBirth(self):
        '''Accessor function to return the hospitals patient date of birth'''
        return self.__patientDateOfBirth

    def setPatientDateOfBirth(self, patientDateOfBirth):
        '''Mutator function to set the hospitals patient date of birth'''
        self.__patientDateOfBirth = patientDateOfBirth
        print("Patient date of birth set...")
        return "Patient date of birth set..."

    def getDailyRate(self):
        '''Accessor function to return the hospitals daily rate of stay'''
        return self.__dailyRate

    def setDailyRate(self, dailyRate):
        '''Mutator function to set the hospitals daily rate of stay'''
        self.__dailyRate = dailyRate
        print("Daily rate set...")
        return "Daily rate set..."

    def getDaysSpentInHospital(self):
        '''Accessor function to return the days spent in the hospital'''
        return self.__daysInHospital

    def setDaysSpentInHospital(self, days):
        '''Mutator function to set the days spent in the hospital'''
        self.__daysInHospital = days
        self.__chargesAccumulator["Daily charges"] = self.__dailyRate * \
            float(days)
        print("Patient days set...")
        return "Patient days set..."

    def getChargesAccumulator(self):
        '''Accessor function to return the current charges for the hospital stay'''
        return self.__chargesAccumulator

    def setChargeToAccumulator(self, product, price):
        '''Mutator function to add an prodcut for the hospital transactions'''
        self.__chargesAccumulator[product] = price
        print("Charge set to accumulator...")
        return "Charge set to accumulator..."

    def deleteChargeFromAccumulator(self, charge):
        '''Mutator function to remove an charge from the hospital transactions'''
        del self.__chargesAccumulator[charge]
        print("Charge removed from accumulator...")
        return "Charge removed from accumulator..."

    def getChargesAccumulatorTotal(self):
        '''Accessor function to return the total of the charges for the hospital stay'''
        charges = 0
        for ctr, product in enumerate(self.__chargesAccumulator):
            charges += self.__chargesAccumulator[product]

        return charges
