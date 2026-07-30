import numpy as np

#Shape 2rows * 3 columns

data=np.array([
    [10,20,30],
    [40, 50, 60]
])
#axis=0: Operate vertically, down the rows.
print(np.sum(data, axis=0)) #[50 70 90]
#axis=1: Operate horizontally across each row.
print(np.sum(data, axis=1)) #[ 60 150]

print(np.mean(data, axis=0)) #[25. 35. 45.]
print(np.mean(data, axis=1)) #[20. 50.]

# Practice Task
sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

# Calculate:
# Total sales for each column
# Total sales for each row
# Average sales for each column
# Average sales for each row
print(f"Total Sales for each column: {np.sum(sales, axis=0)} ")
print(f"Total Sales for each row: {np.sum(sales, axis=1)} ")
print(f"Average Sales for each column: {np.mean(sales, axis=0)} ")
print(f"Average Sales for each column: {np.mean(sales, axis=0)} ")