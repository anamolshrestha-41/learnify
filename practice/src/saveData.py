import numpy as np
import os

os.makedirs('data/processed', exist_ok=True)

def save_dataset(data):
    np.savetxt("data/processed/students_performance.csv", data, delimiter=',', fmt="%s")
    print("Processed dataset saved.")