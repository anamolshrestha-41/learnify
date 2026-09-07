import plotly.express as px
import pandas as pd

def gender_ratio(students):
    gender_count=students['Gender'].value_counts().reset_index()
    gender_count.columns=["Gender", "Count"]
    fig=px.bar(
        gender_count,
        x="Gender",
        y="Count",
        title="Gender Ratio"
    )
    fig.write_image("../outputs/gender.png")
    fig.show()
    return gender_count