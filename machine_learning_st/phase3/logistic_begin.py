import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

data= pd.read_csv("student.csv")
df= pd.DataFrame(data)

X=df[["hours_studied", "attendance"]]
y=df["passed"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
    )

model= LogisticRegression()
model.fit(X_train, y_train)
y_pred= model.predict(X_test)
probability= model.predict_proba(X_test)
print(f"Prediction: {y_pred} and Probability: {probability}")
a_s=accuracy_score(y_test, y_pred)
c_m= confusion_matrix(y_test, y_pred)
print(f"Accuracy: {a_s} and Confusion Metrix: {c_m}")

new_stu=pd.DataFrame({
    "hours_studied": [6],
    "attendance": [80]
})
prediction= model.predict(new_stu)
probability= model.predict_proba(new_stu)
print(f"Result Prediction: {prediction} and Result Probabilites: {probability}")