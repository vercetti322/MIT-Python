# In Part B, we are going to determine how long it will take you to save enough 
# money to make the down payment considering that you get a salary raise after every
# 6 months.

# input function
annual_salary = float(input("Enter your annual salary : "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal : "))
total_cost = float(input("Enter the cost of your dream home : "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal : "))

# calculation of down payment required and current savings initialization
portion_down_payment = 0.25 * total_cost
current_savings = 0
months_required = 0
return_rate = 0.04

# update of current savings as months pass by
while (current_savings <= portion_down_payment):
    current_savings += portion_saved * (annual_salary / 12) + (current_savings * return_rate) / 12
    months_required += 1
    if (months_required % 6 == 0):
        annual_salary += semi_annual_raise * annual_salary

print("Number of months :", months_required)