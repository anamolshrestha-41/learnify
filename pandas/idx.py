import pandas as pd
 #indexing
students= pd.DataFrame({
    'Name': ["Ram", "Hari", "Sita", "Gita"],
    'Age': [20,21,12,13],
    'Marks': [90, 80, 71, 91]
})
# print(students)

#LOC (df.loc[row, column])
print(students.loc[2, "Name"]) #output: sita
# print(students.loc[:, ["Name","Marks"]])#output: names and marks with index
# print(students.loc[:, ["Age","Marks"]])#output: age and marks with index

#ILOC (Position based): df.iloc[row_position,column_position]
print(students.iloc[1,2])#output: 80, row position and column no.. col 2= marks, row 1 = 80
# print(students.iloc[:,:2])#output: names to age with index

#AT  (Fast way to access one single value using labels)
print(students.at[1, 'Age'])

#IAT (fast way to access one value using positions)
print(students.iat[3,2]) #output: gita marks 91


