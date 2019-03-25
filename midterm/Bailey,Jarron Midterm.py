'''
Jarron Bailey
Midterm
Date: March 17th, 2019
Description: This python file returns an amortization payment schedule for a loan
given the Loan Amount, Number of years, and Interst Rate
'''


def numberConverter(number):
    '''Function takes a number and returns a number converted into a int or a float, if parsing fails return string'''
    try:
        number = int(number)
    except ValueError:
        try:
            number = float(number)
        except ValueError:
            number = number
    return number


def isValidNumber(number):
    '''Takes a number and returns True/False depending if the number is either a valid int or float '''
    valid = True
    valid = number.replace(".", "", 1).isdigit()
    number = numberConverter(number)

    if isinstance(number, str):
        valid = False
        return valid
    if number < 0:
        valid = False
    return valid


def getLoanData():
    '''Function collects and return Loan data from user while only accepting "valid inputs from user" '''

    # Loan amount input
    loanAmount = input("\nLoan Amount: ")
    loanAmountValid = isValidNumber(loanAmount)
    loanAmount = numberConverter(loanAmount)
    if loanAmount == 0:
        loanAmountValid = False
    while not loanAmountValid:
        if isinstance(loanAmount, str):
            print("\nLoan Amount must be a number.")
        elif loanAmount <= 0:
            print("\nLoan amount must be greater than 0.")

        loanAmount = input("Loan Amount: ")
        loanAmountValid = isValidNumber(loanAmount)
        loanAmount = numberConverter(loanAmount)

    # Number of years input
    numberOfYears = input("Number of Years: ")
    numberOfYearsValid = isValidNumber(numberOfYears)
    numberOfYears = numberConverter(numberOfYears)
    if numberOfYears == 0:
        numberOfYearsValid = False
    while not numberOfYearsValid:
        if isinstance(numberOfYears, str):
            print("\nNumber of Years must be a number.")
        elif numberOfYears <= 0:
            print("\nNumber of years must be greater than 0.")

        numberOfYears = input("Number of Years: ")
        numberOfYearsValid = isValidNumber(numberOfYears)
        numberOfYears = numberConverter(numberOfYears)

    # Annual interest rate
    annualInterestRate = input("Annual Interest Rate i.e.[7, for 7%]: ")
    annualInterestRateValid = isValidNumber(annualInterestRate)
    annualInterestRate = numberConverter(annualInterestRate)
    if annualInterestRate == 0:
        annualInterestRateValid = False
    while not annualInterestRateValid:
        if isinstance(annualInterestRate, str):
            print("\nAnnual Interest Rate must be a number.")
        elif annualInterestRate <= 0:
            print("\nAnnual Interest Rate must be grater than greater 0%.")

        annualInterestRate = input("Annual Interest Rate: ")
        annualInterestRateValid = isValidNumber(annualInterestRate)
        annualInterestRate = numberConverter(annualInterestRate)

    return {"loanAmount": loanAmount, "numberOfYears": numberOfYears, "annualInterestRate": annualInterestRate}


def calculateMonthLoanDetails(principal, monthlyInterest, monthlyLoanPayment):
    '''
    Function calculates [month interest payment, month principal payment, 
    total monthly loan amount, and new balance] for loan given the [principal, monthly interest rate, and monthly loan payment]
    for a single month, and returns each detail about the loan for the month
    '''

    # Calculate monthly interest payments || principal * interest
    monthInterestPayment = principal * monthlyInterest

    # Total monthly payment || principal + monthly interest payment
    totalMonthlyPayment = principal + monthInterestPayment

    # Calculate monthly principal payments || loan payment - interest payment
    monthPrincipalPayment = monthlyLoanPayment - monthInterestPayment

    balance = totalMonthlyPayment - monthlyLoanPayment

    return {"monthInterestPayment": monthInterestPayment, "monthPrincipalPayment": monthPrincipalPayment, "totalMonthlyPayment": totalMonthlyPayment, "balance": balance}


def formatPaymentsSchedule(data):
    '''Function returns a formated string consisting of the Loan payment schedule,
    take data in the form of a two dimensional array and cycles through each row adding
    each detail in the correct column
    '''
    tabularSchedule = ""
    for i in range(len(data)):
        if i == 0:
            # Header row
            tabularSchedule += '{:<12s}{:<12s}{:<12s}{:<12s}'.format(
                data[i][0], data[i][1], data[i][2], data[i][3])
            tabularSchedule += "\n"
        else:
            # Payments data
            tabularSchedule += '{:<12d}${:<11.2f}${:<11.2f}${:<11.2f}'.format(
                data[i][0], data[i][1], data[i][2], data[i][3])
            tabularSchedule += "\n"
    return tabularSchedule


def calculatePaymentsSchedule(principal, years, annualInterestRate):
    '''
    Function calculates [loan payments, monthly interest payments, monthly principal payments,
    and total loan amount] for loan given the [principal, loan time, and annual interest rate]
    for a single month, and returns each detail about the loan for the period
    '''
    # Principal of Loan
    principal = principal

    # Number of Periodic Payments (n) = Payments per year times number of years
    # 12 payments a year * years
    numOfPayments = 12 * years

    # Periodic Interest Rate (i) = Annual rate divided by number of payment periods
    annualInterestRate = annualInterestRate / 100
    monthlyInterest = annualInterestRate / 12

    # Discount Factor (D) = {[(1 + i) ^n] - 1} / [i(1 + i)^n]
    discountFactor = (((1 + monthlyInterest) ** numOfPayments) - 1) / \
        (monthlyInterest * ((1 + monthlyInterest) ** numOfPayments))

    # Monthly Loan Payment = Principal / Discount Factor or P = A / D
    monthlyLoanPayment = principal / discountFactor

    # Total loan amount || loan payment * number of payments
    totalLoanAmount = monthlyLoanPayment * numOfPayments

    tabularData = []
    columnHeaders = ["Payment#", "Interest", "Principal", "Balance"]
    tabularData.append(columnHeaders)

    # Calculate and append payment details to tabular data array
    for index, payment in enumerate(range(numOfPayments)):
        loanDetails = calculateMonthLoanDetails(
            principal, monthlyInterest, monthlyLoanPayment)
        principal = loanDetails["balance"]
        row = [index + 1, loanDetails["monthInterestPayment"],
               loanDetails["monthPrincipalPayment"], loanDetails["balance"]]
        tabularData.append(row)

    return {"tabularData": tabularData, "totalLoanAmount": totalLoanAmount, "monthlyLoanPayment": monthlyLoanPayment}


def main():
    '''
    Function executes the program.
    Gets loan data from user, validates it, and calculates loan details and payment schedule
    '''
    loanData = getLoanData()
    loanAmount = loanData["loanAmount"]
    numberOfYears = loanData["numberOfYears"]
    annualInterestRate = loanData["annualInterestRate"]

    paymentScheduleDetails = calculatePaymentsSchedule(
        loanAmount, numberOfYears, annualInterestRate)

    paymentsSchedule = formatPaymentsSchedule(
        paymentScheduleDetails["tabularData"])

    print("\nMonthly Payment: {:.2f}".format(
        paymentScheduleDetails["monthlyLoanPayment"]))
    print("Total Payment: {:.2f}".format(
        paymentScheduleDetails["totalLoanAmount"]))
    print("\n" + paymentsSchedule)


main()
