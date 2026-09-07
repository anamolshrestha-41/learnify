import pandas as pd

def merge_dataset(profile_df, stats_df):
    merged_df= pd.merge(profile_df, stats_df, on="player_id")
    return merged_df