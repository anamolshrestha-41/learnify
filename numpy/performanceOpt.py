#NumPy is faster because it performs operations using optimized low-level code.

#only py
# import time 
# numbers= list(range(1_000_000))
# start=time.time()
# result=[]

# for number in numbers:
#     result.append(numbers*2)

# end= time.time()
# print(end - start)

#using numpy
import numpy as np
import time

num= np.arange(1_000_000)
start= time.time()
result= np.multiply(num, 2)
print(result)
end= time.time()
print(end - start)