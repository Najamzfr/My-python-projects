# Importing Libraries
import csv
from tabulate import tabulate

def main():
    # initializing variables
    pv = int(input('Enter principal amount: '))
    i = int(input('Enter interest rate: '))/100
    n = int(input('Enter duration of loan in years: '))

    # calculating PMT
    pmt = cal_PMT(pv, i, n)

    # calculate amortization table
    amortization_schedule = calculate_amortization(pv, i, pmt, n)

    # format it into list
    content = format(amortization_schedule)

    # convert it into tabular form and then print it
    print(convert_to_tabular(content))

'''
This function takes principal amount, interest rate, and the duration of the loan
and then it calculates PMT
'''
def cal_PMT(pv, i, n):
    a = 1 / ((1 + i) ** n)
    b = (1 - a) / i
    pmt = pv / b
    return pmt

# this function then converts it into an amortization table
def calculate_amortization(principal_amount, interest_rate, pmt, n):
    # Create amortization schedule
    schedule = []
    balance = principal_amount
    for year in range(n):
        interest_paid = balance * interest_rate
        principal_paid = pmt - interest_paid
        ending_balance = balance - principal_paid

        schedule.append({
            'Year': year + 1,
            'Beginning Balance': balance,
            'Payment': pmt,
            'Interest Paid': interest_paid,
            'Principal Paid': principal_paid,
            'Ending Balance': ending_balance
        })

        balance = ending_balance

    return schedule

def format(amortization_schedule):
    content = []
    fieldnames = ['Year', 'Beginning Balance', 'Payment', 'Interest Paid', 'Principal Paid', 'Ending Balance']
    content.append(fieldnames)

    for row in amortization_schedule:
        content.append(list(row.values()))

    return content

def convert_to_tabular(file):
    table = tabulate(file, headers="firstrow", tablefmt="grid", floatfmt=".2f")
    return table

if __name__ == "__main__":
    main()
