'''write a program that calculates the minimum fixed monthly payment needed in
   order pay off a credit card balance within 12 months. By a fixed monthly
   payment, we mean a single number which does not change each month, but
   instead is a constant amount that will be paid each month.'''

def pay_in_yr(balance, annIntRate):
    '''from starting balance and annual interest rate, outputs the minimum
       monthly payment that would be required to pay off loan in a year.'''

    #create placeholder for original balance
    orig_balance = balance

    #initialize a payment guess just below the actual value
    payment = balance / 12
    monthly_intrate = annIntRate / 12.0


    while True:
        #loop through a year and estimate ending balance
        for month in range(12):
            unpaid_bal = balance - payment
            interest = unpaid_bal * monthly_intrate
            balance = unpaid_bal + interest

        print("")
        #if ending balance is <=0, solution found, break out
        if balance <= 0:
            break

        #otherwise, reset balance to original_balance, and increment payment guess
        else:
            balance = orig_balance
            payment += 5

    print (int(round(payment, -1)))

pay_in_yr(4773, 0.2)
