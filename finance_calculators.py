# Access two different financial calculators.

import math
# User selecting option of choice

user_selection = input("Please enter option of choice either a 1.investment or 2.bond :")
print(user_selection)

# Conditional Statements

if user_selection == "investment":
    if True:
        principal_amount = float(input("Enter principal amount for investment:"))
        rate = float(input("Enter the interest rate:"))
        r  = (rate/100)

        time = float(input("Enter the duration for investment in years:"))
        interest_type = str(input("Select either a Simple or Compound interest rate:"))

        # There are two types of interest types below.

    if interest_type == "Simple":
        interest_type = principal_amount*(1+r* time)
        total = interest_type

    elif interest_type == "Compound":
         interest_type = principal_amount*(math.pow((1+r), time))
         total = interest_type
    
    print(f"Interest earned over a period of {time} years is: {total}")

#The bond option is alos another conditional statement

if user_selection =="bond":
    if True:
        Present_Value = float(input("Enter the present value amount:"))
        i_rate = float(input("Enter the current interest rate:"))
        i = ((i_rate/100)/12)
        n = float(input("Enter the number of months:"))

# Monthly installments
        month = float(math.floor((i_rate*Present_Value)/1-(1 + i_rate)**(-n)))

    print(f"Monthly repayment is {month}".format())

else:
    print("Invalid Input!")
    
     


#P = intital deposit(given)
#r = interest rate
#t = period of the investment
#A = return on investment after t years
