# It answers: “What is actually happening in this dataset, 
# and what should I do before building an ML model?”

#Finding Pattern: A pattern is something interesting that repeateadly happens in data.
# Examples:
# Sales increase every year.
# Older movies tend to have lower ratings.
#Example:Pattern:Movies are increasing over time.
# Suppose:
# Year	Movies
# 2018	100
# 2019	130 

#Outlier: is a value that is unusally far from the other values.
#Example: 90, 95, 100, 105, 110, 500 .... %100 is suspicious 
# It could be:
# Data entry error
# Genuine unusual observation
# Special case
# You don't automatically delete outliers.
# Q1 = df["duration"].quantile(0.25)
# Q3 = df["duration"].quantile(0.75)
# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
# outliers = df[
#     (df["duration"] < lower) |
#     (df["duration"] > upper)
# ]

# print(outliers)

# 3. Missing Values
# Missing values are values that don't exist.
# Example:
# Title	Country	Rating
# Movie A	USA	PG
# Movie B	India	NaN
# Movie C	NaN	R
# Before ML, you need to understand:
# How many values are missing?
# Which columns have missing values?
# Why are they missing?
# Should they be removed?
# Should they be filled?
# Example
# df.isna().sum()

# 4. Relationships Between Variables
# A relationship means:
# Does one variable change when another variable changes?
# Example:

# Study Hours ↑
#       ↓
# Exam Score ↑

# Potential relationship:

# More study → higher score

# But remember:

# Relationship ≠ causation.

# Example
# df.plot.scatter(
#     x="study_hours",
#     y="score"
# )

# You visually inspect whether the points form a pattern.


# 5. Skewness
# Concept

# Skewness tells you whether a distribution is symmetric or pulled toward one side.

# Three important cases
# Normal:

#       █
#      ███
#     █████
#    ███████
#   █████████

# Approximately symmetric.

# Right-skewed
# ████████
# █████
# ███
# ██
# █

# Long tail → right side.

# Common examples:

# Income
# House prices
# Sales
# Left-skewed

# Long tail → left side.

# Example
# print(df["duration"].skew())

# Rough interpretation:

# ≈ 0       → approximately symmetric
# > 0       → right-skewed
# < 0       → left-skewed
# Your task

# Choose a numerical column.

# Calculate skewness.
# Plot histogram.
# Determine the distribution shape.
# Explain why it might be skewed.

# 6. Feature Distribution

# Before ML, you need to understand how each feature is distributed.

# For example:

# Age
# 18  19  20  21  22 ...

# You want to know:

# Minimum
# Maximum
# Mean
# Median
# Spread
# Distribution
# Outliers
# Skewness
# Example
# df["duration"].describe()

# And:

# df["duration"].hist()

# You combine statistics + visualization.

# Your task

# Choose 3 numerical features.

# For each:

# df[column].describe()

# Then create a histogram.

# Record:

# Mean
# Median
# Min
# Max
# Standard deviation
# Skewness
# Distribution shape


# 7. Correlation Analysis

# Correlation measures how strongly two numerical variables move together.

# Usually:

# +1 → strong positive relationship
#  0 → no linear relationship
# -1 → strong negative relationship

# Example:

# Study Hours ↑
# Score       ↑

# Correlation → +0.85
# Example
# corr = df.corr(numeric_only=True)

# print(corr)

# Visualization:

# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.heatmap(corr, annot=True)

# plt.show()
# Your task

# Create a correlation matrix.

# Find:

# Strongest positive correlation.
# Strongest negative correlation.
# Weak relationships.
# Features that may contain redundant information.

# 8. Business Insights

# This is where EDA becomes real data analysis.

# Don't just say:

# "Comedy has 1,200 titles."

# Ask:

# "What does this mean for the business?"

# Example

# Suppose Netflix data shows:

# Drama       → 1,500
# Comedy      → 1,200
# Documentary → 700
# Horror      → 400

# Basic observation:

# Drama is the most common genre.

# Business insight:

# Drama represents a major portion of the content catalog, suggesting Netflix has historically invested heavily in drama content.

# Then ask:

# Should Netflix continue investing in drama?

# Now EDA is helping decision-making.

# Your task

# For every major analysis, write:

# Observation:
# What does the data show?

# Interpretation:
# Why might this be happening?

# Business implication:
# Why does this matter?

# 9. EDA Workflow

# This is the workflow I recommend you practice repeatedly:

#         Dataset
#            ↓
#    Understand the Data
#            ↓
#     Data Quality Check
#            ↓
#     Missing Values
#            ↓
#       Duplicates
#            ↓
#      Data Types
#            ↓
#    Descriptive Statistics
#            ↓
#  Feature Distributions
#            ↓
#       Outliers
#            ↓
#       Relationships
#            ↓
#       Correlation
#            ↓
#      Find Patterns
#            ↓
#     Business Insights
#            ↓
#    Prepare for Machine Learning

# The important thing is that EDA is not just making graphs.

# It is a process of asking questions and using the data to answer them.