import pandas as pd

# Applies a function to a Series or DataFrame.
empl=pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Salary": [10000, 20000, 50000],
    # "Gender": ["Male", "Female", "Gay"]
})
empl["Bonus"]=empl["Salary"].apply(lambda x: x*0.1)
print(empl)

# Maps values.
# print(empl["Gender"].map({
#     "Male": 0,
#     "Female":2,
#     "Gay": 1
# }))

#applymap() : Applies to every element in a DataFrame.
# emplz= empl.applymap(str.upper)
# print(emplz)

empl["Adding five"]= empl["Salary"].apply(lambda x: x+5)
print(empl)

conv=pd.DataFrame({
    "Condition": ["Yes", "No"]
})

res=conv["Condition"].map({
    "Yes": 1,
    "No": 0
})
print (res)