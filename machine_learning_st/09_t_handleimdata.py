from sklearn.datasets import make_classification
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.metrics import classification_report, balanced_accuracy_score, average_precision_score
X, y = make_classification(
    n_samples=500,
    n_features=5,
    n_informative=3,
    n_redundant=0,
    random_state=42
)

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
#normal model
normal_model=LogisticRegression(max_iter=1000)
normal_model.fit(X_train, y_train)
normal_pred= normal_model.predict(X_test)
#weighted model
weighted_model=LogisticRegression(class_weight="balanced", max_iter=1000)
weighted_model.fit(X_train, y_train)
weighted_pred=weighted_model.predict(X_test)
#SMOTE
smote_model=Pipeline([
    ("smote", SMOTE(random_state=42)),
    ("model", LogisticRegression(max_iter=1000))
])
smote_model.fit(X_train, y_train)
smote_pred= smote_model.predict(X_test)
models={
    "Normal":(normal_model, normal_pred),
    "Weighted":(weighted_model, weighted_pred),
    "SMOTE":(smote_model, smote_pred)
}

for name, (model, predictions) in models.items():
    print(name)
    print(classification_report(y_test, predictions))
    print(balanced_accuracy_score(y_test, predictions))
    probabilities= model.predict_proba(X_test)[:,1]
    print(f"Average Precision: {average_precision_score(y_test, probabilities)}")