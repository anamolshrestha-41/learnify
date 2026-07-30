#Eigen is a vector whose direction doesnot change after multiplication by the matrix
# The eigenvalue tells us how much the vector is scaled.
# This is important in:
# PCA
# Dimensionality Reduction
# Data Science
# Physics
# Machine Learning

import numpy as np
matrix= np.array([
    [4,0],
    [0,3]
])
eigenvalues, eigenvectors= np.linalg.eig(matrix)
print(f"Eigen Value: {eigenvalues}")
print(f"Eigen Vectors: {eigenvectors}")

mat= np.array([
    [3,1],
    [0,2]
])
print(np.linalg.eig(mat))