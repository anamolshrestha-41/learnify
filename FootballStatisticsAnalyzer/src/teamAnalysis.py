import pandas as pd
import numpy as np

def club_statistics(df):
    stats=(
        df.groupby("Club").agg(
            Most_Goals=("Goals", "sum"),
            Average_Rating=("Rating", np.mean),
            Most_Players=("Player", "count"),
            Average_Age=("Age", np.mean),
            Highest_Market_Value=("Market Value", "max"),
        ).sort_values(by="Most_Goals", ascending=False)
    )
    return stats

def country_statistics(df):
    stats=(
        df.groupby("Country").agg(
            Most_Goals=("Goals", "sum"),
            Average_Rating=("Rating", np.mean),
            Most_Players=("Player", "count"),
            Average_Age=("Age", np.mean),
            Highest_Market_Value=("Market Value", "max"),
        ).sort_values(by="Most_Goals", ascending=False)
    )
    return stats

def position_statistics(df):
    stats=(
        df.groupby("Position").agg(
            Most_Goals=("Goals", "sum"),
            Average_Rating=("Rating", np.mean),
            Most_Players=("Player", "count"),
            Average_Age=("Age", np.mean),
            Highest_Market_Value=("Market Value", "max"),
        ).sort_values(by="Most_Goals", ascending=False)
    )
    return stats