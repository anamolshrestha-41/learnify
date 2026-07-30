#numpy stores arrays in memory in an organized way.
import numpy as np
arr= np.arange(1_000_000, dtype=np.int64)
print(f"Shape: {arr.shape}")
print(f"Memory: {arr.nbytes}")
print(f"Datatype: {arr.dtype}")
print(f"Strides: {arr.strides}")