import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from lightgbm import LGBMClassifier
import shap
X, y=make_classification(
    n_samples=200,
    n_features=4,
    n_redundant=0, 
    n_informative=3,
    random_state=42
)
feature_names=["recent_form", "defensive_strength", "attacking_strength", "possession"]
X=pd.DataFrame(X, columns=feature_names)
X_train, X_test, y_train, y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model=LGBMClassifier(n_estimators=100, learning_rate=0.05, num_leaves=5, max_depth=4, colsample_bytree=0.9, reg_alpha=0.1, reg_lambda=1, random_state=42, verbosity=-1, min_child_samples=5)
model.fit(X_train, y_train)
explainer= shap.TreeExplainer(model)
shap_values=explainer(X_test)
print(shap_values.shape)
shap.plots.waterfall(shap_values[0])
shap.plots.bar(shap_values)
# Dependency plot for possession
shap.plots.scatter(shap_values[:, feature_names[3]])
shap.plots.scatter(
    shap_values[:, "recent_form"],
    color=shap_values[:, "defensive_strength"]
)
#automatic interaction coloring
shap.plots.scatter(shap_values[:,feature_names[1]], color= shap_values)
#comparing multiple features.
for feature in feature_names:
    shap.plots.scatter(
        shap_values[:, feature]
    )