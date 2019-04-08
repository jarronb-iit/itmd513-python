'''
Jarron Bailey
Homework 9
Date: April 8th, 2019
Description: This program illustrates the use of classes by building a coffee
vending machine application
'''
from VendingMachine import VendingMachine


def main():
    '''Function instantiate a vending machine and passes user inputs'''
    purchase = ""
    VendingMachine1 = VendingMachine(1, 2)
    quarters = input("How many quarters are you inserting: ")
    dimes = input("How many dimes are you inserting: ")
    nickels = input("How many nickels are you inserting: ")
    VendingMachine1.insert(quarters, dimes, nickels)
    while(True):
        ifPurchase = input("Purchase?\n1: yes and 2: No\n")
        if ifPurchase == "1":
            purchase = "yes"
            break
        if ifPurchase == "2":
            purchase = "no"
            break
        print("Please enter 1 or 2.\n")
    if purchase == "yes":
        VendingMachine1.select()
    else:
        VendingMachine1.refund()


main()
