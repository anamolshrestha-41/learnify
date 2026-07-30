import numpy as np

def analysis_data(data):
    print('--Data Analysis--')

    hrs= data[:,1]>5
    highStudy= data[hrs]
    print(f'Students studing more than 5 hrs: {len(highStudy)}')

    sleep= data[:,3].astype(float)
    low_sleep= data[sleep<6]
    print(f'Students sleeping less than 6 hrs: {low_sleep}')

    atten= data[:,2]>90
    highAttendance=data[atten]
    print(f'High Attendance Students: {highAttendance}')

    highMarkks= data[data[:,6].argsort()[-10:][::-1]] 
    print(f'Top 10 high marks Students: {highMarkks}')

    worstMarks= data[data[:,6].argsort()[:10]]
    print(f'Worst 10 students (Lowest marks): {worstMarks}')

    average_attendance= np.mean(data[:,2])
    print(f'Average Attendance: {average_attendance}')   

    average_phoneuse= np.mean(data[:,4])
    print(f'Average Phone Use: {average_phoneuse}')

    with open("reports/report.txt", "w") as file:
        file.write('Student report\n')
        file.write(f'Total Students: {len(data)}')
        file.write(f'High study Hours: {highStudy}')
        file.write(f'Low sleep : {low_sleep}')
        file.write(f'Average phone Use: {average_phoneuse}')
        file.write(f'Average attendance: {average_attendance}')
        
    print("Report generated Successfully!")


    return data