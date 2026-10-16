import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

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
print(f"Intercept: {model.intercept_} and Coefficient: {model.coef_[0]}")

for feature, coefficient in zip(X.columns, model.coef_[0]):
    odd_ratio= np.exp(coefficient)
    print(f"{feature}: {odd_ratio}")

proba= model.predict_proba(X_test)[:,1]
for threshold in [0.3, 0.5, 0.7]:
    y_pred=(proba>=threshold).astype(int)
    print(f"Threshold: {threshold}\n Accuracy: {accuracy_score(y_test, y_pred)}\n Precision: {precision_score(y_test, y_pred)}\n Recall: {recall_score(y_test, y_pred)}")