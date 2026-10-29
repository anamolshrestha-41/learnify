import pandas as pd
datas = {
    "player_id": [
        "P01", "P02", "P03", "P04", "P05",
        "P06", "P07", "P08", "P09", "P10",
        "P11", "P12", "P13", "P14", "P15",
        "P16", "P17", "P18", "P19", "P20"
    ],

    "match_date": [
        "2026-01-01", "2026-01-02", "2026-01-03",
        "2026-01-04", "2026-01-05", "2026-01-06",
        "2026-01-07", "2026-01-08", "2026-01-09",
        "2026-01-10", "2026-01-11", "2026-01-12",
        "2026-01-13", "2026-01-14", "2026-01-15",
        "2026-01-16", "2026-01-17", "2026-01-18",
        "2026-01-19", "2026-01-20"
    ],

    "team_id": [
        "T1", "T1", "T2", "T2", "T3",
        "T3", "T1", "T2", "T3", "T1",
        "T2", "T3", "T1", "T2", "T3",
        "T1", "T2", "T3", "T1", "T2"
    ],

    "minutes_played": [
        40, 35, 30, 38, 25, 40, 32, 36, 28, 40,
        34, 22, 37, 29, 40, 31, 39, 26, 35, 33
    ],

    "shots": [
        8, 6, 5, 9, 4, 10, 7, 6, 5, 11,
        8, 3, 9, 4, 10, 6, 9, 4, 7, 8
    ],

    "shots_on_target": [
        4, 3, 2, 5, 2, 6, 4, 3, 2, 7,
        4, 1, 5, 2, 6, 3, 5, 2, 4, 4
    ],

    "passes_completed": [
        25, 20, 18, 28, 15, 30, 22, 24, 17, 32,
        26, 12, 27, 16, 29, 21, 31, 14, 23, 25
    ],

    "distance_km": [
        4.2, 3.8, 3.1, 4.5, 2.7, 4.8, 3.6, 4.0, 3.0, 4.9,
        4.1, 2.4, 4.4, 3.2, 4.7, 3.5, 4.6, 2.8, 3.9, 4.0
    ],

    "goals_scored": [
        2, 1, 0, 3, 1, 4, 2, 1, 0, 4,
        2, 0, 3, 1, 3, 1, 4, 0, 2, 2
    ]
}
df=pd.DataFrame(datas)
X=df[["minutes_played", "shots", "shots_on_target", "passes_completed", "distance_km"]]
y=df["goals_scored"]

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.ensemble import RandomForestRegressor 
X_train, X_test, y_train, y_test=train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.2
)
kf=KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
model=RandomForestRegressor(
    n_estimators=100,
    max_depth=3,
    random_state=42
)
score=cross_val_score(
    model,
    X,
    y,
    cv=kf, #cross validation
    scoring="neg_mean_absolute_error"
)

mae_scores=-score
print(f"AVERAGE MAE: {round(mae_scores.mean(), 2)}")
print(f"Standard Deviation: {round(mae_scores.std(), 2)}")