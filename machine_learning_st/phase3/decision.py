from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
import matplotlib.pyplot as plt


iris= load_iris(as_frame=True)
df= iris.frame
X= df.drop(columns="target")
y= df["target"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

for max_depth in [2, 5]:
    model=DecisionTreeClassifier(
        max_depth=max_depth,
        criterion="gini",
        random_state=42
    )
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    print(f"Training accuracy: {model.score(X_train, y_train)}")
    print(f"Testing accuracy: {model.score(X_test,y_test)}")

    plt.figure(figsize=(12,6))
    plot_tree(
        model,
        feature_names=X.columns,
        class_names=iris.target_names,
        filled=True,
        rounded=True
    )
    plt.show()
    model_2=DecisionTreeClassifier(
            max_depth=max_depth,
            criterion="entropy",
            random_state=42
        )
    model_2.fit(X_train, y_train)
    y_pred_2= model_2.predict(X_test)
    print(f"Training accuracy: {model_2.score(X_train, y_train)}")
    print(f"Testing accuracy: {model_2.score(X_test,y_test)}")

    plt.figure(figsize=(12,6))
    plot_tree(
        model_2,
        feature_names=X.columns,
        class_names=iris.target_names,
        filled=True,
        rounded=True
    )
    plt.show()