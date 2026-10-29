import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

X,y= make_classification(
    n_samples=500,
    n_features=3,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    weights=[0.65, 0.35],
    class_sep=1.0,
    random_state=42
)
X=pd.DataFrame(
    X,
    columns=["shot_distance", "shot_angle", "under_pressure"]
)

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

results=[]

for depth in [1, 2, 3, 5, 10, None]:
    model=DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )
    score=cross_val_score(
        model, X_train, y_train, cv=5, scoring="f1"
    )
    print(f"Depth: {depth}, Mean F1: {score.mean()}")
    results.append((depth, score.mean()))

best_depth, best_f1= max(
    results,
    key=lambda item:item[1]
)

best_model=DecisionTreeClassifier(
    max_depth=best_depth,
    random_state=42
)

best_model.fit(X_train, y_train)
test_predictions= best_model.predict(X_test)

print(f"Best Depth: {best_depth}, Best CV F1: {round(best_f1,3)}")
print(classification_report(y_test, test_predictions))