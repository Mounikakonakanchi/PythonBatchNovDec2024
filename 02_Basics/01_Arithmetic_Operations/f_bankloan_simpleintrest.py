""""
Algorithm:
step1: Declare the Principal amount,annual interest rate,
      duration of the loan.
step2: Calcute the the Simple Interest rate.
step3: Add Simple Interest rate with the Principal 
       amount.
step4: Display the final amount.

"""

# Initialise the Variables 
principal_amount = float(input("Please Enter the Loan Amount(Principal):"))
annual_interest = float(input("Please Enter the Anuual Interest Rate(in %):"))
duration_of_loan = float(input("Please Enter the Loan In Years(In Years) :"))

# Simple Interest Calculation
simple_interest = (principal_amount*annual_interest*duration_of_loan)/100
print("Simple Interest     :",simple_interest)

# compute the total payable amount
final_amount = principal_amount+simple_interest
print("Final Amount   :",final_amount)