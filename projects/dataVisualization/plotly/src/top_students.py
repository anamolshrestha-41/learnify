import plotly.express as px

def top_students(students):
    top_10= students.sort_values('Grade', ascending=False).head(10)
    fig= px.bar(
        top_10, x="Grade",
        y="Name", orientation="h",
        title="Top 10 Students by Grade"
    )
    fig.write_image("../outputs/top_students.png")
    fig.show()
    return top_10