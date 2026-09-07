import plotly.express as px 

#Plotly makes graphs interactive
#Insetad of pictures, we get hover, zoom, oan, download, fullscreen

#Interactive Charts: Same graph interactive
# fig= px.line(
#     x=[1,2,3,4],
#     y=[2,4,6,8]
# )
# fig.show() #Output: A line graph with the specified data points, but interactive

#Create interactive attendance chart
# attendance=[80, 85, 90, 95, 100, 75, 70]
# days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# figure= px.line(
#     x=days,
#     y=attendance,
#     labels={
#         'x': "Days of the Week",
#         'y': "Attendance (%)"
#     },
#     title="Weekly Attendance" 
# )
# figure.update_yaxes(range=[0, 100])
# figure.show() #Output: A line graph with the specified data points, but interactive

#hover: move mouse
# figr= px.bar(
#     x=["Apples", "Bananas", "Cherries"],
#     y=[70, 85, 90]
# )
# figr.show()
#Another eg: Create interactive student marks chart.
# fig= px.bar(
#     x=["Anamol", "Dikshya", "Us"],
#     y=[90, 91, 100]
# )
# fig.show()

#Dashboard: Instead of one graph, Show many together.
#Example: Attendance, Grades, Age, Gender, Top Students all in one page.
#Usually: plotly.subplots or Dash

# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
# #row/col tells where to place the graph
# fig= make_subplots(
#     rows=2,
#     cols=2,
#     specs=[
#         [{"type": "xy"}, {"type": "domain"}],
#         [{"type": "xy"}, {"type": "xy"}]
#     ]
# )
# # fig.add_trace(
# #     go.Bar(
# #         x=["Apples", "Bananas", "Cherries"],
# #         y=[100, 90, 80]
# #     ),
# #     row=1, col=1
# # )
# # fig.add_trace(
# #     go.Scatter(
# #         x=[1,2,3,4],
# #         y=[10, 20, 30, 40]
# #     ),
# #     row=2, col=1
# # )
# # fig.show() #Output: A dashboard with 2 graphs, one bar chart and one line chart, both interactive

# fig.add_trace(
#     go.Bar(
#         x=["s1a","s2b", "s3c"],
#         y=[90, 80, 70]
#     ),
#     row=1, col=1
# )
# fig.add_trace(
#     go.Pie(
#         labels=["s1a","s2b", "s3c"],
#         values=[90, 80, 70]
#     ),
#     row=1, col=2
# )
# fig.add_trace(
#     go.Histogram(
#         x=[1,2,3,4,5,6,7,8,9,10],
#         y=[10,20,30,40,50,60,70,80,90,100]
#     ),
#     row=2, col=1
# )
# fig.add_trace(
#     go.Line(
#         x=[1,2,3,4,5],
#         y=[10,20,30,40,50]
#     ),
#     row=2, col=2
# )
# fig.show()

#Animation: Show changes over time
# df= px.data.gapminder()
# fig= px.scatter(
#     df, x="gdpPercap", y="lifeExp", animation_group="year", animation_frame="year", hover_name="country", color='continent'
# )
# fig.show()
#Another example: Animate monthly attendance.
import pandas as pd
df= pd.DataFrame({
    "month":[
        "Jnuary", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ],
    "attendance":[
        80, 85, 90, 95, 100, 75, 70, 85, 90, 95, 100, 80
    ]
})

fig=px.bar(
    df, x="month", y="attendance", title="Monthly Attendance", animation_group="month", color="attendance"
)
fig.show()