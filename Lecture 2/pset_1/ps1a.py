# In Part A, we are going to determine how long it will take you to save enough 
# money to make the down payment.

# input function
annual_salary = float(input("Enter your annual salary : "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal : "))
total_cost = float(input("Enter the cost of your dream home : "))

# calculation of down payment required and current savings initialization
portion_down_payment = 0.25 * total_cost
current_savings = 0
months_required = 0
return_rate = 0.04

# update of current savings as months pass by
while (current_savings <= portion_down_payment):
    current_savings += portion_saved * (annual_salary / 12) + (current_savings * return_rate) / 12
    months_required += 1

print("Number of months :", months_required)