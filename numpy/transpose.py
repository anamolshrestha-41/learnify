import numpy as np

#transpose changes rows into columns.
matrix= np.array([
    [1,2,3],
    [4,5,6]
])
print(matrix.T)
#OR
print(np.transpose(matrix))
data=np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
print(np.transpose(data))