from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
X,y = make_classification(
    n_samples=500,
    n_features=3,
    n_informative=3,
    n_redundant=0,
    weights=[0.65, 0.35],
    random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

model=DecisionTreeClassifier(random_state=42)
param_distributions={
    "max_depth": randint(2,20),
    "min_samples_split":randint(2,20),
    "min_samples_leaf": randint(1,10)
}
cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

random_search= RandomizedSearchCV(
    estimator=model,
    param_distributions=param_distributions,
    n_iter=30,
    cv=cv,
    scoring="f1",
    random_state=42,
    n_jobs=-1,
    refit=True
)
random_search.fit(X_train, y_train)
print(random_search.best_params_)
print(random_search.best_score_)
best_model= random_search.best_estimator_

y_pred= best_model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["No Goal", "Goal"]))
print(confusion_matrix(y_test, y_pred))