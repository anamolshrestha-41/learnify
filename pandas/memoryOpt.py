import pandas as pd

# Large datasets may have millions of rows. Optimizing memory speeds up processing and can prevent out-of-memory errors

df = pd.DataFrame({
    "Age": [25, 32, 45, 18, 60],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "City": ["Kathmandu", "Pokhara", "Kathmandu", "Lalitpur", "Pokhara"]
})

print(df.dtypes)
#astype(): Change a column's data type
df["Age"]= df["Age"].astype("int8")
df["Gender"] = df["Gender"].astype("category")
df["City"] = df["City"].astype("category")

#check memory usage
print(df.info(memory_usage="deep"))
# OR df.memory_usage(deep=True)

print(df)
print(df.dtypes)
