import numpy as np
a = -1
b = -5
c = 6

delta = b**2 - 4*a*c

x1 = (-b + np.sqrt(delta))/(2*a)
x2 = (-b - np.sqrt(delta))/ (2*a)

print("x1 = {} \n x2 = {}".format(x1, x2))