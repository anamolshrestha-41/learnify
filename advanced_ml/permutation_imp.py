import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.inspection import permutation_importance
X, y= make_classification(
    n_samples=1000,
    n_features=4,
    n_informative=4,
    n_redundant=0,
    random_state=42
)
features=["recent_form", "attack_strength", "defence_strength", "home_advantages"]
X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model=XGBClassifier(n_estimators=200, learning_rate=0.04, reg_alpha=0.1, reg_lambda=1, subsample=1)
model.fit(X_train, y_train)
results=permutation_importance(
    model,
    X_test,
    y_test,
    n_repeats=10, 
    scoring="f1",
    random_state=42,
    n_jobs=-1
)

importance_df=pd.DataFrame({
    "Features": features,
    "Importance": results.importances_mean,
    "STD": results.importances_std
}).sort_values(by="Importance", ascending=False)
print(importance_df)