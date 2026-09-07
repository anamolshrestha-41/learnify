import pandas as pd
import numpy as np

def top_goal_scorers(df):
    df=df.sort_values(by="Goal", ascending= False).head()
    return df

def top_assists(df):
    df=df.sort_values(by="Assists", ascending=False).head(10)
    return df

def high_rating(df):
    df=df.sort_values(by="Rating", ascending=False).head(10)
    return df

def player_statistics(df):
    stats={
        "Average Goals" : np.mean(df["Goals"]),
        "Average Rating": np.mean(df["Rating"]),
        "Oldest Player": df.sort_values(by="Age", ascending=False).head(1),
        "Youngest Player": df.sort_values(by="Age").head(1),
        "Highest Minutes Played": df.sort_values(by="Minutes Played", ascending=False).head(1),
        "Top 10 Players": df.nlargest(10, "Goals"),
        "Total Goals": np.sum(df["Goals"]),
        "Median Goals": np.median(df["Goals"]),
        "Goal Standard Deviation": np.std(df["Goals"]),
        "90th Percentile Goals": np.percentile(df["Goals"], 90)
    }
    return stats