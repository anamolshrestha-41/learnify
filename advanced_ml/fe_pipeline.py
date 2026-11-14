from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "goals": [5,3,2,7],
    "shots": [10, 15, 8, 9],
    "under_pressure": [0, 1, 0, 1],
    "venue": ["Dreams Sindhu", "Hope RIse", "Balkot_Sports", "Gurkhas"]
})
X=df.drop(columns="goals")
y=df["goals"]
X_train, X_test, y_train, y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

numerical_features=["shots", "under_pressure"]
categorical_features=["venue"]

numerical_transformer=Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer=Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor=ColumnTransformer([
    ("num", numerical_transformer, numerical_features),
    ("cat", categorical_transformer, categorical_features)
])

model=Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(random_state=42))
])
model.fit(X_train, y_train)
prediction= model.predict(X_test)
print(f"ACTUAL: {y_test.values}")
print(f"Predication: {prediction}")