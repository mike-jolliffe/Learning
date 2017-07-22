'''Write a program to calculate the credit card balance after one year if a
   person only pays the minimum monthly payment required by the credit
   card company each month.'''

def cc_bal(balance, annIntRate, monthlyPaymentRate, months):
    '''given a starting balance, an annual interest rate, required
       monthly minimum payment, and months outputs the remaining balance after
       that many months'''

    #estimate min payment, unpaid balance @ month's end, interest that accrued on
    #unpaid balance and new balance for start of following month
    min_payment = balance * monthlyPaymentRate
    unpaid_bal = balance - min_payment
    interest = (annIntRate/12.0) * unpaid_bal
    balance = round(unpaid_bal + interest, 2)

    #while months are still ongoing, decrement by one and call cc_bal again
    while months > 1:
        months -= 1
        return cc_bal(balance, annIntRate, monthlyPaymentRate, months)

    print ("Remaining balance: {}".format(balance))

cc_bal(484, 0.2, 0.04, 12)
