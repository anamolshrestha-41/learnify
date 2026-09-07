import numpy as np
import pandas as pd

def remove_duplicates(df):
    clean= pd.drop_duplicates(df)
    return clean

def fill_missing_values(df):
    df.replace(["?", "-", "NaN"], np.nan, inplace=True)
    df["Age"]=df["Age"].fillna(df["Age"].mean())
    df["Club"]=df["Club"].fillna("Unknown")
    return df

def rename_columns(df):
    df= df.rename(columns={
        "Player Name": "player_name"
    })
    return df

def convert_datatypes(df):
    df["Age"]=df["Age"].astype(int)
    df["Goals"]=df["Goals"].astype(int)
    return df

def remove_invalid_rows(df):
    invalid_rows= np.where((df["Age"]<0)|(df["Goals"]<0))[0]
    df= df.frop(index=invalid_rows)
    return df

def clean_dataset(df):
    df= remove_duplicates(df)
    df= fill_missing_values(df)
    df= rename_columns(df)
    df= convert_datatypes(df)
    df= remove_invalid_rows(df)

    df= df.reset_index(drop=True)
    return df