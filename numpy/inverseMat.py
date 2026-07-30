# The inverse of a matrix is similar to the reciprocal of a number.

# For a number:

# 5 × 1/5 = 1

# For a matrix:

# A × A⁻¹ = I

# where I is the identity matrix.

import numpy as np

matrix=np.array([
    [2,1],
    [5,3]
])
inverse = np.linalg.inv(matrix)
print(inverse)
#Check
identity= matrix@inverse
print(identity)