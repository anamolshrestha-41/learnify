import pandas as pd
import matplotlib.pyplot as plt
#just using plotly
import plotly.express as px

df= pd.DataFrame({
    "title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E",
              "Movie F", "Movie G", "Movie H"],
    "duration": [90, 100, 110, 95, 105, 120, 115, 300]
})

Q1= df["duration"].quantile(0.25)
Q3= df["duration"].quantile(0.75)
IQR= Q3-Q1
lower= Q1-1.5*IQR
upper= Q3+1.5*IQR
outlier= df[
    (df["duration"]<lower)| (df["duration"]>upper)
]
print("Q1", Q1)
print("Q2", Q3)
print("lower", lower)
print("upper", upper)
print(outlier)
print(outlier[["title", "duration"]])

plt.figure(figsize=(10, 7))
plt.boxplot(df["duration"])
plt.ylabel("Duration")
plt.title("Netflix Duration Boxplot")
plt.show()

#plotly
fig=px.box(df, y="duration")
fig.show()