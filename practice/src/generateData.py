import numpy as np
import os 

#for class 11-12
def generate_data():

    np.random.seed(40)
    students = 200
    age= np.random.randint(14, 18, students)
    study_hrs= np.random.uniform(1, 8, students) #floatings
    attendamce= np.random.randint(20, 80, students) # 20 to 80 percent attendance
    sleep= np.random.uniform(1, 8, students)
    phone= np.random.uniform(1,8, students)
    assignment= np.random.randint(1, 5, students) # total 5 assignments
    midterm= np.random.randint(30, 50, students) #pass 30, full-50
    finalTerm= np.random.randint(45, 100, students)

    dataSet= np.column_stack((
        age, study_hrs, attendamce, sleep, phone, assignment, midterm, finalTerm
    ))
    os.makedirs("data/raw", exist_ok=True)
    np.savetxt("data/raw/studentsData.csv", dataSet, delimiter=",", fmt="%.2f")
    print("Random data generated.")
    return dataSet