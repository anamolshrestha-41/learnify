import numpy as np

def feature_engineering(data):
    print('--Feature Engineering--')

    average_Marks=(data[:,5]+data[:,6]+data[:,7])/3
    study_efficiency=average_Marks/data[:,1]

    risk=((average_Marks<50) & (data[:,2]<70))

    risk_level= np.where(risk, 'HighRisk', 'Safe')

    performance= np.where(
        average_Marks>=85, 'Excellent',
        np.where(
            average_Marks>=70, 'Good',
            np.where(
                average_Marks>=50, 'Average',
                'Poor'
            )
        )
    )

    data=np.column_stack((data, average_Marks, study_efficiency, risk ))
    print('New Shape')
    print(data.shape)

    return data