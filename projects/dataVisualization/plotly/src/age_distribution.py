import plotly.express as px

def age_distribution(students):
    mean_age= students["Age"].mean()
    median_age= students["Age"].median()
    fig= px.histogram(
        students, x="Age", title="Age Distribution"
    )
    fig.write_image("age_distribution.png")
    fig.show()
    return mean_age, median_age
