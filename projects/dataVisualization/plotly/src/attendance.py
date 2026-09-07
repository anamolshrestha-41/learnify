import plotly.express as px
def attendance(students):
    #attendance avg, high, low
    average= students['Attendance'].mean()
    highest= students['Attendance'].max()
    lowest= students['Attendance'].min()
    fig= px.line(
        students,
        x="Name",
        y="Attendance",
        title="Student Attendance",
        markers=True
    )
    fig.write_image("../outputs/attendance.png")
    fig.show()
    return average, highest, lowest