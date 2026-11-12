import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier


df = pd.DataFrame({
    "shot_distance": [2, 5, 3, 8, 6, 4, 9, 2, 7, 5,
                      3, 8, 4, 6, 10, 2, 5, 7, 3, 9],
    "shot_angle": [30, 45, 25, 60, 50, 35, 65, 20, 55, 40,
                   28, 62, 33, 48, 70, 22, 42, 58, 27, 68],
    "under_pressure": [0, 1, 0, 1, 1, 0, 1, 0, 1, 0,
                       0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    "goal": [1, 0, 1, 0, 0, 1, 0, 1, 0, 1,
             1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
})
X=df[["shot_distance", "shot_angle", "under_pressure"]]
y=df["goal"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

dt=DecisionTreeClassifier(random_state=42)
rf=RandomForestClassifier(n_estimators=200, random_state=42)
gb=GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=4, random_state=42)
xgb= XGBClassifier(n_estimators=200, learning_rate=0.05, max_depth=4, eval_metric='logloss',random_state=42)
lgbm=LGBMClassifier(n_estimators=100, learning_rate=0.05, num_leaves=15,reg_alpha=0.1, reg_lambda=1, random_state=42)
models = {
    "Decision Tree": dt,
    "Random Forest": rf,
    "Gradient Boosting": gb,
    "XGBoost": xgb,
    "LightGBM": lgbm
}

importance_results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    importance = model.feature_importances_

    for feature, score in zip(X_train.columns, importance):

        importance_results.append({
            "Model": name,
            "Feature": feature,
            "Importance": score
        })

importance_df = pd.DataFrame(importance_results)

print(importance_df)

