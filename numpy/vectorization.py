#Vectorization means performing operations on entire arrays instead of using loops.

import numpy as np

numbers=[1,2,3,4,5]
result= numbers * 2
print(result) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
num=np.array([1,2,3,4,5])
print(num*2) #[ 2  4  6  8 10]

#Apply a 15% discount to every price.
prices= np.array([100, 200, 300, 400])
dicountedPrice= prices * 0.85
print(dicountedPrice)