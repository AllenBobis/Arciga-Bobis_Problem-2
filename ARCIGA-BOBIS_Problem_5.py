# Import_libraries
import matplotlib.pyplot as plt
import numpy as np
from math import *
# Set range
N = np.arange(200).tolist()
val = np.zeros(200)

X = input('Input Equation for x(n): ')
def F(n):
    return eval(X)

for n in range(200):
    val[n] = F(n)
# Input values of x and y
x = np.sin(val)
y = np.zeros(200)
y[0] = -1.5*x[0] + 2*x[1] - 0.5*x[2]
for i in range(1, 199):
    y[i] = 0.5*x[i+1] - 0.5*x[i-1]
y[199] = 1.5*x[199] - 2*x[198] + 0.5*x[197]
# Plot using stem()
plt.stem(N,y, 'b', markerfmt='bo', label='y(n)', use_line_collection=True)
plt.stem(N, x, 'r', markerfmt='ro', label='x(n)', use_line_collection=True)
plt.legend()
plt.xlabel('n')
plt.ylabel('Magnitude') 
plt.title('Graph of x(n) and y(n)')
plt.show()