#Jemal Beshir 118799384
import math
def get_min_payment(principal, annual_interest_rate, loan_term=30, payments_per_yr=12):
    P = principal
    r = annual_interest_rate/payments_per_yr
    n = loan_term*payments_per_yr
    A = (P*r*(1+r)**n)/(((1+r)**n)-1)
    return math.ceil(A)
#notes
#uses, mortgage amount as principal, annual interest rate, loan term, and payments per yr

def interest_due(current_balance, annual_interest_rate, payments_per_yr=12):
    b = current_balance
    r = annual_interest_rate/payments_per_yr
    i = b*r
    return i

def remaining_payments(current_balance, annual_interest_rate, target_payment, payments_per_yr=12):
    counter = 0
    while current_balance > 0:
        interest = interest_due(current_balance, annual_interest_rate, payments_per_yr)
        principal_amount = target_payment-interest
        if(principal_amount <=0):
            break
        current_balance = current_balance - principal_amount
        counter+=1
    return counter


#Notes:
#use if and else
#Calculate interest using interest_due(), subtract the rest from the balance, count how many payments it takes to pay it off

def main(principal, annual_interest_rate, loan_term=30, payments_per_yr=12, target_payment=None):
    min_payment = get_min_payment(principal, annual_interest_rate, loan_term=30, payments_per_yr=12)
    print(f"Your minimum payment is:  ${min_payment}")
    if (target_payment == None):
        target_payment = min_payment

    if (target_payment < min_payment):
        print("Your target payment is less than the minimum payment for this mortgage")
    else:
        total_num_req = remaining_payments(principal, annual_interest_rate, target_payment, payments_per_yr=12)
        print(f"If you make payments of ${target_payment} , you will pay off the mortgage in {total_num_req} payments.")
#notes
#use get_min_payment
#show the remaining payments and print it out.
