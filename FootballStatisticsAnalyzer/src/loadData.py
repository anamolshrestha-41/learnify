import pandas as pd

def load_data(profile_path, stats_path):
    try:
        profile_df= pd.read_csv(profile_path)
        stats_df= pd.read_csv(stats_path)
        print("Data loaded!!")
        return profile_df, stats_df

    except FileExistsError:
        print("Dataset not found.")
        return None, None

    except Exception as e:
        print(e)
        return None, None

def dataset_info(df, name):
    print(name.upper())
    print("Shape:" , df.shape)
    print("Columns",df.columns.tolist())
    print("Data Types",df.dtypes)
    print("Memory usage",df.memory_usage(deep=True))
    print(" Missing values ",df.isnull().sum())
    print("Duplicate Rows",df.duplicated().sum())

def first_rows(df, rows=5):
    print(df.head(rows))

def last_rows(df, rows=5):
    print(df.tail(rows))

def dataset_summary(df):
    print(df.describe(include="all"))


# if __name__=="__main__":

#     profile_path,stats_path = load_data(
#         "../datas/all_player_profiles.csv",
#         "../datas/all_player_stats.csv")
#     if profile_path is not None:

#         dataset_info(profile_path, "Player Profile")

#         first_rows(profile_path)

#         dataset_summary(profile_path)

#     if stats_path is not None:

#         dataset_info(stats_path, "Player Statistics")

#         first_rows(stats_path)

#         dataset_summary(stats_path)