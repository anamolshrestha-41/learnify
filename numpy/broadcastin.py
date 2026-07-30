import numpy as np

#Concept: Broadcasting allows numpy to perform operations on arrays with different shapes.
#Instead of manually looping through every value, NumPy automatically expands smaller arrays when possible.
data= np.array([
    [10,20,30],
    [40,50,60]
])
increase= np.array([1,2,3])
result= increase+data
print(result) #[[11 22 33] [41 52 63]]

temperatures= np.array([
    [20,25,30],
    [22,27,32],
    [18, 24, 29]
])
correction= np.array([2,-1,3])
res=temperatures+correction
print(res)