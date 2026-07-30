import numpy as np

def statistics_data(data):
    print('--Statistics--')
    print(f' Average Age: {np.mean(data[:, 0])} ')
    print(f' Average sleep: {np.mean(data[:, 3])} ')
    print(f'Mid value of sleep: {np.median(data[:,3])}')
    print(f'Variance in MidTerm: {np.var(data[:,6])}')
    print(f'Standard Deviation of studyHrs: {np.std(data[:, 1])}')
    print(f'Max Num in Final: {np.max(data[:,7])}')
    print(f'Correlation: {np.corrcoef(data[:,3], data[:,4])}')
    print(f'Covariance: {np.cov(data[:, 0], data[:, 1])}')

    return data