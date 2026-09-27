import pandas as pd


data = {
    "hours_studied": [
        2.5, 4.0, 6.5, 3.0, 8.0, 5.5, 1.5, 7.0, 4.5, 9.0,
        3.5, 6.0, 2.0, 7.5, 5.0, 8.5, 3.0, 6.5, 4.0, 9.5,
        2.5, 5.5, 7.0, 1.0, 8.0, 4.5, 6.0, 3.5, 7.5, 5.0
    ],

    "attendance": [
        65, 72, 85, 68, 92, 78, 55, 88, 74, 95,
        70, 82, 60, 90, 76, 93, 64, 80, 71, 97,
        62, 79, 86, 50, 91, 73, 84, 67, 89, 77
    ],

    "previous_score": [
        58, 64, 75, 60, 88, 70, 52, 81, 67, 90,
        62, 73, 55, 84, 69, 86, 57, 78, 65, 94,
        59, 72, 80, 48, 87, 63, 76, 61, 83, 71
    ],

    "final_score": [
        61, 68, 82, 63, 91, 76, 50, 85, 70, 94,
        66, 79, 56, 88, 73, 92, 59, 81, 67, 96,
        58, 75, 84, 45, 90, 69, 80, 64, 87, 74
    ]
}

df= pd.DataFrame(data)
print(df.head(10))
print(df.shape)

#Feature and Target
X= df[[
    "hours_studied", "attendance", "previous_score"
]]
y=df["final_score"]

#Train Test Split
from sklearn.model_selection import train_test_split as tts
X_train, X_test, y_train, y_test= tts(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#Model creation
from sklearn.linear_model import LinearRegression
model= LinearRegression()
model.fit(X_train, y_train)
y_predict= model.predict(X_test)

#Evaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
mae= mean_absolute_error(y_test, y_predict)
mse= mean_squared_error(y_test, y_predict)
rmse= mse ** 0.5
r2= r2_score(y_test, y_predict)

print("Coefficient: ", model.coef_[0])
print("Intercept: ", model.intercept_)

print("\nEvaluation")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)

#Actual vs Predicted
result=pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_predict
})

print(result)

#Visualization
import plotly.express as px

fig= px.scatter(
    result,
    x="Actual",
    y="Predicted",
    title="Actual vs Predicted Final Score"
)
fig.show()