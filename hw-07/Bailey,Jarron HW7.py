'''
Jarron Bailey
Homework 7
Date: March 7th
Description: This python file returns an converted Phone number to the console which depends
on the alphanumeric characters entered
'''

import re


def isValid(phone_number):
    '''
    Function returns True or False, function takes a phone number and check to see if 
    its only alphanumeric character and only the correct length
    '''
    isValidBool = True
    if len(phone_number) != 12:
        print("\nThe correct format of the number is XXX-XXX-XXXX, dashes included")
        print("Here")
        isValidBool = False
    elif True:
        phone_number = phone_number.replace("-", "", 2)
        if not bool(re.match('^[a-zA-Z0-9]+$', phone_number)):
            print("\nThe correct format of the number is XXX-XXX-XXXX, dashes included")
            print("X being alphanumeric characters")
            isValidBool = False
    return isValidBool


def translatePhoneNumber(phone_number):
    '''
    Function returns a phone number depending on the alphanumberic characters entered
    '''
    phone_number = phone_number.upper()
    phone_table = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', '222333444555666777788899990123456789')
    print(phone_number.translate(phone_table))
    phone_number = phone_number.translate(phone_table)
    return phone_number


def main():
    '''
    Runs function to receive number, pass it to the validation function which then
    passes the validated number to translate function which returns an translated string
    that will be outputted to the console
    '''
    phone_number = input("Hi, Please enter telephone number(XXX-XXX-XXXX): ")
    valid = isValid(phone_number)

    while not valid:
        if not valid:
            phone_number = input(
                "\nPlease enter telephone number(XXX-XXX-XXXX): ")
        valid = isValid(phone_number)

    phone_number = translatePhoneNumber(phone_number)
    return print("Here's your translated telephone number : {}".format(phone_number))


# Run Program
main()
