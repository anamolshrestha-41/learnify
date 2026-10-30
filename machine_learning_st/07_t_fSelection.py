from sklearn.datasets import make_classification
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.model_selection import train_test_split

# Simulated football shot data
X, y = make_classification(
    n_samples=500,
    n_features=5,
    n_informative=3,
    n_redundant=0,
    random_state=42
)

feature_names = [
    "shot_distance",
    "shot_angle",
    "goalkeeper_position",
    "defensive_pressure",
    "player_experience"
]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

selector= SelectKBest(
    score_func=mutual_info_classif,
    k=3
)
X_train_selected= selector.fit_transform(X_train, y_train)
X_test_selected= selector.transform(X_test)

selected_features=[
    name for name, keep in zip(feature_names, selector.get_support()) if keep
]
print("Selected features:", selected_features)
print("Original feature count:", X_train.shape[1])
print("Selected feature count:", X_train_selected.shape[1])

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

model= RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rfe= RFE(
    estimator=model,
    n_features_to_select=3
)
rfe.fit(X_train, y_train)
print([name for name, keep in zip(
    feature_names,
    rfe.support_
) if keep ])

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

model=make_pipeline(
    StandardScaler(),
    LogisticRegression(
        l1_ratio=1,
        solver="liblinear",
        C=0.1,
        random_state=42
    )
)
model.fit(X_train, y_train)
coefficients=model.named_steps["logisticregression"].coef_[0]