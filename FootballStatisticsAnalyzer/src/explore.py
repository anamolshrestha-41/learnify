import numpy as np

def basic_statistics(df):
    print("Basic Statistics")

    print(f"Dataset Shape: {df.shape}")
    print(f"Columns: {df.columns}")
    print(f"Dataset Info: {df.info()}")

    print(f"Total Players: {df.shape[0]}")
    print(f"Total Clubs: {df['Club'].nunique()}")
    print(f"Total Countries: {df['Country'].nunique()}")
    print(f"Unique Positions: {df['Position'].nunique()}")

    print(f"Average Age {np.mean(df['Age'])}")
    print(f"Maximum Goals {np.max(df['Goals'])}")
    print(f"Minimum Goals {np.min(df['Goals'])}")
    print(f"Average Rating {np.average(df['Rating'])}")

def missing_values(df):
    print(f"Missing Values in every column {df.isnull()}")
    print(f"Total Missing Values {df.isnull().sum()}")

def duplicate_rows(df):
    print(f"Duplicate rows: {df.duplicated()}")
    print(f"Total duplicated rows: {df.duplicated().sum()}")

def unique_values(df):
    print(f"Actual unique values {df["Country"].unique()}")
    print(f"Frequency of Countries {df["Country"].value_counts()}")

def numerical_summary(df):
    print(f"Describe: {df.describe()}")
    print(f"Average Ages: {np.mean(df["Age"])}")
    print(f"Mid value of age: {np.median(df["Age"])}")
    print(f"Max goals: {np.max(df["Goals"])}")
    print(f"Variation in Ratings: {np.std(df["Rating"])}")
    print(f"percentage of values (Ratings) in a dataset that fall below a particular value. {np.percentile(df["Rating"], 50)}")


def categorical_summary(df):
    print(f"Unique Categories: {df['Category'].nunique()}")
    print(f"Most common categories: {df['Category'].value_counts()}")
    print(f"Frequency of Goals: {df["Goals"].unique()}")
