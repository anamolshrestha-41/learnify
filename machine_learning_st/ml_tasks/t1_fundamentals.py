import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error as mae, mean_squared_error as mse, r2_score as r2s

data={
     "student_id": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30
    ],

    "hours_studied": [
        2.5, 4.0, 6.5, 1.5, 8.0, 5.0, 3.0, 7.5, 4.5, 9.0,
        2.0, 6.0, 5.5, 3.5, 7.0, 1.0, 8.5, 4.0, 6.5, 2.5,
        5.0, 7.5, 3.0, 9.5, 4.5, 6.0, 2.0, 8.0, 5.5, 7.0
    ],

    "attendance": [
        75, 82, 91, 68, 95, 88, 72, 93, 85, 97,
        65, 89, 84, 76, 92, 60, 96, 81, 90, 73,
        87, 94, 70, 98, 83, 86, 62, 95, 88, 91
    ],

    "previous_score": [
        58, 65, 72, 50, 81, 69, 55, 78, 67, 85,
        48, 74, 70, 61, 76, 45, 88, 64, 79, 57,
        71, 82, 53, 91, 66, 73, 49, 84, 77, 80
    ],

    "final_score": [
        62, 70, 78, 52, 88, 75, 59, 84, 72, 92,
        50, 81, 76, 66, 83, 47, 94, 69, 85, 61,
        77, 89, 57, 96, 71, 79, 54, 91, 82, 87
    ]
}

df= pd.DataFrame(data)

#Feature and Target
X=df[[
    "hours_studied",
    "attendance",
    "previous_score"
]]
y=df["final_score"]

#Train/Test Split
X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
#debugging things
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)

print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

print("X_train type:", type(X_train))
print("X_test type:", type(X_test))

print("y_train type:", type(y_train))
print("y_test type:", type(y_test))

#Baseline
baseline= DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train)
baseline_pred= baseline.predict(X_test)

#ML model
model= LinearRegression()
model.fit(X_train, y_train)
y_pred= model.predict(X_test)

#Evaluation
MAE= mae(y_test, y_pred)
MSE= mse(y_test, y_pred)
root_mse= MSE ** 0.5
r2= r2s(y_test, y_pred)

print("Baseline MAE: ", mae(y_test, baseline_pred))
print("Model MAE: ", MAE)
print("Model MSE: ", MSE)
print("Model Root Mean Squared Error: ", root_mse)
print("Model R_square: ", r2)
