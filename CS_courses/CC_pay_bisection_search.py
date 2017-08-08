'''Use bisection search to calculate the smallest monthly payment such that we
   can pay off the entire credit card balance within a year.'''

def cc_payoff(balance, annIntRate):
    #create placeholder for original balance
    orig_balance = balance

    #establish monthly intrate, lower bound and upper bound for guess
    monthly_intrate = annIntRate / 12.0
    payment_lwr_bound = balance / 12.0
    payment_upr_bound = (balance * (1 + monthly_intrate)**12) / 12.0
    payment = (payment_upr_bound + payment_lwr_bound) / 2

    while True:
        #loop through a year and estimate ending balance
        for month in range(12):
            unpaid_bal = balance - payment
            interest = unpaid_bal * monthly_intrate
            balance = unpaid_bal + interest

        print("")
        #if ending balance == 0, solution found, break out
        if balance > -.01 and balance < .01:
            break

        #otherwise, reset balance to original_balance, and increment payment guess
        elif balance > 0:
            balance = orig_balance
            payment_lwr_bound = payment
            payment = (payment_upr_bound + payment_lwr_bound) / 2

        else:
            balance = orig_balance
            payment_upr_bound = payment
            payment = (payment_upr_bound + payment_lwr_bound) / 2

    print (round(payment, 2))

cc_payoff(320000, 0.2)
