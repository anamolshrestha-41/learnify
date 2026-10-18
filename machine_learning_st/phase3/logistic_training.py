import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

iris=load_iris(as_frame=True)
df= iris.frame
print(df.head())

X= df.drop(columns="target")
y=df["target"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    stratify=y,
    test_size=0.2,
    random_state=42
)
model_l1=Pipeline([
    ("scaler", StandardScaler()),
    ("logistic", LogisticRegression(
            l1_ratio=1,
            solver="saga",
            C=1.0,
            max_iter=1000
    ))
])
model_l2= Pipeline([
    ("scaler", StandardScaler()),
    ("logistic", LogisticRegression(
        l1_ratio=0,
        solver="lbfgs",
        C=1.0,
        max_iter=1000
    ))
])
model_l1.fit(X_train,y_train)
model_l2.fit(X_train, y_train)
l1_coef= model_l1.named_steps["logistic"].coef_[0]
l2_coef= model_l2.named_steps["logistic"].coef_[0]
print(f" L1 coefficient: {l1_coef} ")
print(f" L2 coefficient: {l2_coef} ")

model_l1_pred= model_l1.predict(X_test)
model_l2_pred= model_l2.predict(X_test)
print(f"L1 Accuracy: {accuracy_score(y_test, model_l1_pred)} and L2 Accuracy: {accuracy_score(y_test, model_l2_pred)}")
print(f"L1 classification report: {classification_report(y_test, model_l1_pred, target_names=iris.target_names, zero_division=0)}")
print(f"L2 classification report: {classification_report(y_test, model_l2_pred, target_names=iris.target_names, zero_division=0)}")

new_flower = pd.DataFrame({
    "sepal length (cm)": [5.1],
    "sepal width (cm)": [3.5],
    "petal length (cm)": [1.4],
    "petal width (cm)": [0.2]
})

prediction_l1=model_l1.predict(new_flower)[0]
prediction_l2=model_l2.predict(new_flower)[0]

probability_l1= model_l1.predict_proba(new_flower)[0]
probability_l2= model_l2.predict_proba(new_flower)[0]

print("L1 predicted species:", iris.target_names[prediction_l1])
print("L2 predicted species:", iris.target_names[prediction_l2])

print("\nL1 probabilities:")
for species, probability in zip(iris.target_names, probability_l1):
    print(f"{species}: {probability:.2%}")

print("\nL2 probabilities:")
for species, probability in zip(iris.target_names, probability_l2):
    print(f"{species}: {probability:.2%}")