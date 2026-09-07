import pandas as pd

def preprocess_data(students):

    # Remove duplicates
    students= students.drop_duplicates()
    # Clean text columns
    students['Name']= students['Name'].str.strip();
    # Convert numerical columns
    students['Age']= pd.to_numeric(students['Age'])
    # Handle missing values
    students= students.dropna()
    # Validate values
    students= students[students['Age']>0]

    return students