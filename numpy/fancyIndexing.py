import numpy as np
 # Fancy indexing allows you to select multiple positions using an array of indexes.

numbers= np.array([10,20,30,40,50])
indexes=[0,2,4]
print(numbers[indexes]) #10 30 50

#For 2d
matrix= np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

rows=[0,2]
column=[1,2]

print(matrix[rows, column]) #20, 90


# Practice Task
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
# Select:
# 10
# 50
# 90
# using fancy indexing.
row=[0,1,2]
column=[0,1,2]
print(data[row, column])