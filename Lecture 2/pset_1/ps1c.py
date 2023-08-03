# 1. Your semi­annual raise is .07 (7%) 
# Your investments have an annual return of 0.04 (4%)  
# The down payment is 0.25 (25%) of the cost of the house 
# The cost of the house that you are saving for is $1M. 
 
# You are now going to try to find the best rate of savings to 
# achieve a down payment on a $1M house in 36 months.

# input function
annual_salary = float(input("Enter the starting salary : "))

# calculation of down payment required and current savings initialization
total_cost = 1000000
portion_down_payment = 0.25 * total_cost
months_required = 36
return_rate = 0.04
semi_annual_raise = 0.07
initial_salary = annual_salary

# Implementation of logic
front = 0
end = 10000
counter = 0
found_rate = False

while (front <= end):
    mid = int(front + (end - front) / 2)
    current_savings = 0
    for i in range(1, 37):
        current_savings += (mid / 10000) * (annual_salary / 12)
        current_savings += (current_savings * return_rate) / 12
        if (i % 6 == 0):
            annual_salary *= semi_annual_raise + 1
            
    if (abs(current_savings - portion_down_payment) <= 100):
        found_rate = True
        print("Best savings rate : ", (mid / 10000))
        print("Steps in Bisection search : ", counter)
        break
        
    elif ((current_savings - portion_down_payment) > 100):
        end = mid
        counter += 1
        
    else:
        front = mid
        counter += 1
    
    annual_salary = initial_salary
    
if not found_rate:
    print("It is not possible to pay the down payment in 36 months.")