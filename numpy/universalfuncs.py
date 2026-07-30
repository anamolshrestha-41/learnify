import numpy as np

#uNIVERSAL functions perform mathematical operations element-by-element on numPy arrays.
# np.sqrt()
# np.exp()
# np.log()
# np.sin()
# np.cos()
# np.abs()
# np.round()

numbers= np.array([1,4,9,16, 25])
result= np.sqrt(numbers)
print(result)
print(np.square(numbers))
print(np.exp(numbers))
print(np.log(numbers))
print(np.sin(numbers))
num= np.array([-10, -5, 0, 5, 10])
print(np.abs(num))
print(np.round(numbers))