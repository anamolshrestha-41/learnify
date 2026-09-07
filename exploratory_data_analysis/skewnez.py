import pandas as pd
import plotly.express as px

df= pd.DataFrame({
        "year": [2020, 2021, 2022, 2023, 2024],
        "population":[1000, 2000, 1980, 2412, 2913]
})

skewness= df["population"].skew()
print(skewness)

fig= px.histogram(
    df,
    x="population",
    title="Distribution of population"
)
fig.show()