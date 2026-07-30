#Matrix multiplication is different from element-by-element multiplication.

import numpy as np

# Element-wise Multiplication
# A * B
# Matrix Multiplication
# A @ B
# or:
# np.matmul(A, B)

mat1= np.array([
    [1,2],
    [3,4]
])
mat2= np.array([
    [5,8],
    [6,7]
])
res= mat1@mat2
print(res)
print(np.matmul(mat1, mat2))