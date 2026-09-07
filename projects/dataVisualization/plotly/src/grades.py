import plotly.express as px

def grade(students):
    average_grade= students['Grade'].mean()
    top_ten= students.sort_values('Grade', ascending=False).head(10)
    fig= px.bar(
        top_ten,
        x="Name",
        y="Grade",
        title="Top 10 students by grade"
    )
    fig.write_image("../outputs/grades.png")
    fig.show()
    return average_grade, top_ten