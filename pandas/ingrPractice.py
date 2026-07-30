import pandas as pd

employees= pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Department": ["IT","HR","IT","Sales","HR","Sales"],
    "Salary": [50000, 40000, 60000, 45000, 42000, 483820]
})
print('===EASY===')
print(f'Only Salary using loc')
print(employees.loc[:, "Salary"]) #Only salary
print(f'Show first three rows using iloc')
print(employees.iloc[:3])
print('Get Cs salary using at.')
print(employees.at[2, "Salary"])
print('Get Ds department using iat.')
print(employees.iat[3,1])
print('===MEDIUM===')
print('Average salary of each department')
print(employees.groupby("Department")['Salary'].mean())
print('Maximum salary of each department.')
print(employees.groupby("Department")["Salary"].max())
print('Count employees in each department.')
print(employees.groupby("Department")["Name"].count())
print("Add department average salary using transform().")
employees["Average"]= employees.groupby('Department')['Salary'].transform("mean")
print(employees)
print(employees.groupby("Department").filter(lambda x: x["Salary"].sum()>45000))