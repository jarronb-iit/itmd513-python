'''
Jarron Bailey
Final Assignments
Date: May 6th, 2019
Description: This program is to present a GUI that computes a patient’s bill for a hospital stay.
A GUI that allows the user to enter a type of surgery and a type of medication, and check the patient 
out of the hospital. When the patient checks out, the total charges should be displayed in a Window 
format (GUI Interface).
'''


class Surgery:
    '''
    Class is responsible for handling information pertaining to the different types of surgeries
    the hospital offers and the price of each procedure
    '''

    def __init__(self):
        '''Constructor initializes the surgeries and their prices'''
        self.__surgeries = {
            "Heart valve replacement": 170000,
            "Spinal fusion": 110000,
            "Hip replacement": 40364,
            "Gastric bypass": 25000,
            "Knee replacement": 35000
        }

    def getSurgeries(self):
        '''Accessor function to surgeries dataset'''
        return self.__surgeries
