import numpy as np
# The dot product multiplies corresponding values and adds them together.

# Mathematically:
# [1, 2, 3] · [4, 5, 6]
# = 1*4 + 2*5 + 3*6
# = 32

a=np.array([1,2,3,4])
b=np.array([2,4,6,8])
print(np.dot(a,b))

# In Machine Learning, dot products are used in:

# input features × weights

weights= np.array([0.5, 0.3, 0.2])
features= np.array([10, 20, 30])
print(np.dot(weights, features))