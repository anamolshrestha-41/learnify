# Your task

# Using a dataset:

# Group data by year.
# Count records per year.
# Plot the result.
# Write 2–3 observations.

import pandas as pd
import matplotlib.pyplot as plt

# df= pd.DataFrame({
#     "year": [2020, 2020, 2021, 2021, 2022, 2023, 2023]
# })

# count= df.groupby("year").size()

# count.plot(kind="bar")
# plt.xlabel("Year")
# plt.ylabel("Records")
# plt.title("Records per Year")
# plt.show()

import plotly.express as px

df= pd.DataFrame({
    "year": [2020, 2020, 2021, 2021, 2022, 2023, 2023]
})

count= df.groupby("year").size().reset_index(name="records")

fig= px.bar(count,
x="year",
y="records",
title="Records per year")

fig.show()