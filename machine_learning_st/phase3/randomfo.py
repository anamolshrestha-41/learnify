from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import pandas as pd
#Loading dataset
iris= load_iris(as_frame=True)
df=iris.frame
#Feature and Target
X= df.drop(columns="target")
y= df["target"]
#Train&Test
X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    stratify=y,
    random_state=42,
    test_size=0.2
)

for n in [50, 100]:
    model=RandomForestClassifier(
        n_estimators=n,
        max_depth=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    # Training and Testing Accuracy
    print(f"Traning Accuracy: {model.score(X_train, y_train)}")
    print(f"Testing Accuracy: {model.score(X_test, y_test)}")
    importance= pd.Series(
        model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)
    importance.sort_values().plot(kind="bar")
    plt.title("Random Forest Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.show()

    new_flower = pd.DataFrame({
    "sepal length (cm)": [5.1],
    "sepal width (cm)": [3.5],
    "petal length (cm)": [1.4],
    "petal width (cm)": [0.2]
    })
    prediction=model.predict(new_flower)[0]
    probabilities=model.predict_proba(new_flower)[0]
    print("Predicted species:", iris.target_names[prediction])

    for species, probability in zip(iris.target_names, probabilities):
        print(f"{species}: {probability:.2%}")