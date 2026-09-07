import pandas as pd
import plotly.express as px

df= pd.DataFrame({
        "year": [2020, 2021, 2022, 2023, 2024],
        "population":[1000, 2000, 1980, 2412, 2913]
})
print(df)
fig=px.scatter(df,x="year", y="population")
fig.show()