from load_data import load_data
from preprocessing import preprocess_data
from attendance import attendance
from grades import grade
from gender import gender_ratio
from age_distribution import age_distribution
from top_students import top_students
from dashboard import create_dashboard

def main():
    students= load_data("../data/students.csv")
    students=preprocess_data(students)
    import os
    os.makedirs("../outputs", exist_ok=True)

    attendance(students)
    grade(students)
    gender_ratio(students)
    age_distribution(students)
    top_students(students)

    create_dashboard(students)

    print("Student analysis Dashboard created successfully!!")

if __name__=="__main__":
    main()