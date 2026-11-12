from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

X, y = make_classification(
    n_samples=1000,
    n_features=4,
    n_informative=4,
    n_redundant=0,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
importance=pd.DataFrame({
    "Features":["shot_distance", "shot_angle", "defensive_pressure", "goalkeeper_distance"],
    "Importance":model.feature_importances_
}).sort_values(by="Importance", ascending=False)
print(importance)