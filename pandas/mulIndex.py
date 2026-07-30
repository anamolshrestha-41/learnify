import pandas as pd


#multiple index: Sometimes one index isnot enough
sales= pd.DataFrame({
    "Year": [2024, 2024, 2025],
    "Month": ["Jan", "feb", "Jan"],
    "Sales": [200, 300, 250]
})
#set_index
indx= sales.set_index(["Year", "Month"])
print(indx)
#rest_index(): returns normal DataFrame
print(sales.reset_index())

employees= pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Department": ["IT","HR","IT","Sales","HR","Sales"],
    "Salary": [50000, 40000, 60000, 45000, 42000, 483820]
})
eIndx= employees.set_index(["Name", "Department"])
print(eIndx)
print(employees.reset_index())