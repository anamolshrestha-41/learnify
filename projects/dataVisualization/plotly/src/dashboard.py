import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
os.makedirs("outputs", exist_ok=True)

def create_dashboard(students):
    #Attendance Trend
    attendance= students.groupby("StudentID")["Attendance"].mean().reset_index()
    #Grade
    grade_distribution= students["Grade"].value_counts().sort_index()

    #Gender ratio
    gender_count= students["Gender"].value_counts()

    #Age distribution
    age_count= students["Age"]

    #top 10
    top_10= students.sort_values('Grade', ascending= False).head(10)

    #create Dashboard
    fig= make_subplots(
        rows=3,
        cols=2,
        specs=[
            [{"type": "xy"}, {"type": "xy"}],
            [{"type": "domain"}, {"type": "xy"}],
            [{"type": "xy"}, None]
        ],
        subplot_titles=[
            "Attendance Trend",
            "Grade Distribution",
            "Gender Ratio",
            "Age Distribution",
            "Top 10 Students by Grade"
        ]
    )

    #Attendance line chart
    fig.add_trace(
        go.Scatter(
            x= attendance["StudentID"],
            y= attendance["Attendance"],
            mode="lines+markers",
            name="Attendance"
        ), 
        row=1, col=1
    )
    #Grade Bar chart
    fig.add_trace(
        go.Bar(
            x= grade_distribution.index,
            y= grade_distribution.values,
            name="Students"
        ), 
        row=1, col=2
    )
    # Gender pie chart
    fig.add_trace(
        go.Pie(
            labels=gender_count.index,
            values=gender_count.values,
            name="Gender"
        ),
        row=2, col=1
    )

    # Age histogram
    fig.add_trace(
        go.Histogram(
            x=age_count,
            name="Age"
        ),
        row=2, col=2
    )

    # Top 10 horizontal bar chart
    fig.add_trace(
        go.Bar(
            x=top_10["Grade"],
            y=top_10["Name"],
            orientation="h",
            name="Grade"
        ),
        row=3, col=1
    )

    fig.update_layout(
        title="Students Performance Dashobard",
        height=1000,
        showlegend=False
    )
    fig.write_html("dashboard.html")
    fig.show()
    return fig