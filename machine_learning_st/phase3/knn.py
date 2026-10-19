import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris= load_iris(as_frame=True)
df= iris.frame
print(df.head())
X= df.drop(columns="target")
y= df["target"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

for k in [3, 7]:
    model= Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=k))
    ])
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

    new_flower = pd.DataFrame({
        "sepal length (cm)": [5.1],
        "sepal width (cm)": [3.5],
        "petal length (cm)": [1.4],
        "petal width (cm)": [0.2]
    })
    prediction= model.predict(new_flower)[0]
    print("Predicted species:", iris.target_names[prediction])