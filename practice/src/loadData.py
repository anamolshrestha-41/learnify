import numpy as np

def load_dataset():
    data= np.loadtxt('data/raw/studentsData.csv',delimiter=",")

    print(f'Shape: {data.shape}')
    print(f'Size: {data.size}')
    print(f'Dimension: {data.ndim}')
    print(f'Data Type: {data.dtype}')
    print()
    print(f'First 12 rows: {data[:12]} ')

    return data