# A Very Simple Program: Raising a number to a power and taking a logarithm
import numpy as np

x = input("Please enter the number 'x': ")
y = input("Please enter the number 'y': ")
z = int(x) ** int(y)
print("z is x raised to the power y : ", z)
log = np.log(int(z)) / np.log(2)
print("log is the logarithm to the base 2 of z : ", log)

