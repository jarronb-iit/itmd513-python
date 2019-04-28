'''
Jarron Bailey
Homework 11
Date: May 6th, 2019
Description: This program is to present a GUI that computes a patient’s bill for a hospital stay.
A GUI that allows the user to enter a type of surgery and a type of medication, and check the patient
out of the hospital. When the patient checks out, the total charges should be displayed in a Window
format (GUI Interface).
'''


class Pharmacy:
    '''
    Class is responsible for handling information pertaining to the different types of medication
    the hospital offers and the price of each prescription
    '''

    def __init__(self):
        '''Constructor initializes the medications and their prices'''
        self.__medications = {
            "Synthroid (levothyroxine)": 38.07,
            "Crestor (rosuvastatin)": 500.19,
            "Ventolin HFA (albuterol)": 50.00,
            "Nexium (esomeprazole)": 238.12,
            "Advair Diskus (fluticasone)": 16.00
        }

    def getMedications(self):
        '''Accessor function to medications dataset'''
        return self.__medications
