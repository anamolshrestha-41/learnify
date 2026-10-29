import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay, roc_auc_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

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
baseline= DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)
baseline_pred= baseline.predict(X_test)
print(f"Baseline Accuracy : {accuracy_score(y_test, baseline_pred)}")

models={
    "logistic":make_pipeline(
        StandardScaler(),
        LogisticRegression(random_state=42)
    ),
    "random":RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}
cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
scoring = {
    "accuracy": "accuracy",
    "precision": "precision",
    "recall": "recall",
    "f1": "f1",
    "roc_auc": "roc_auc"
}
results=[]
for name, model in models.items():
    scores=cross_validate(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring=scoring
    )
    results.append({
        "Model":name,
        "Accuracy":scores["test_accuracy"].mean(),
        "Precision":scores["test_precision"].mean(),
        "Recall":scores["test_recall"].mean(),
        "F1":scores["test_f1"].mean(),
        "ROC-AUC": scores["test_roc_auc"].mean()
    })
results_df=pd.DataFrame(results)
print(results_df.round(3))

best_name=results_df.loc[results_df["F1"].idxmax(), "Model"]
best_model=models[best_name]
print(f"Selected best model: ", best_name)

best_model.fit(X_train, y_train)
y_pred= best_model.predict(X_test)
y_prob=best_model.predict_proba(X_test)[:,1] #class 1
print(classification_report(y_test, y_pred))
print("Test ROC-AUC", round(roc_auc_score(y_test, y_pred),3))
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred, display_labels=["No Goal", "Goal"]
)
plt.title(f"Final Test Result- {best_name}")
plt.tight_layout()
plt.show()
