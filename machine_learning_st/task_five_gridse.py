from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split , GridSearchCV , StratifiedKFold

X,y= make_classification(
    n_samples=500,
    n_features=3,
    n_redundant=0,
    n_informative=3,
    weights=[0.65, 0.35],
    random_state=42
)
X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

from sklearn.tree import DecisionTreeClassifier

param_grids={
    "max_depth": [2,3,4,5,10, None],
    "min_samples_split":[2, 5, 10],
    "min_samples_leaf":[1, 2, 4]
}

cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
model=DecisionTreeClassifier(random_state=42)

grid_search=GridSearchCV(
    estimator=model,
    param_grid=param_grids,
    scoring="f1",
    cv=cv,
    n_jobs=-1,
    refit=True
)
grid_search.fit(X_train, y_train)
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Cross Validation F1: {round(grid_search.best_score_, 3)}")
best_model=grid_search.best_estimator_

from sklearn.metrics import classification_report, confusion_matrix
test_pred= best_model.predict(X_test)
print(classification_report(y_test, test_pred, target_names=["No goal", "Goal"]))
print(f"Confusion Matrix: {confusion_matrix(y_test, test_pred)}")