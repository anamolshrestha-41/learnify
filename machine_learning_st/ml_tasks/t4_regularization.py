import pandas as pd
from  sklearn.model_selection import train_test_split 
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data={
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

X= df[[
    "hours_studied", "attendance", "previous_score"
]]

y=df["final_score"]

X_train, X_test, y_train, y_test= train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

models=[
    ("Linear", None, LinearRegression()),
    ("Ridge", 0.01, Ridge(alpha=0.01)),
    ("Ridge", 0.1, Ridge(alpha=0.1)),
    ("Ridge", 1, Ridge(alpha=1)),
    ("Ridge", 10, Ridge(alpha=10)),
    ("Ridge", 100, Ridge(alpha=100))
]

result=[]
for name, alpha, model in models:
    model.fit(X_train, y_train)
    ypred= model.predict(X_test)
    mae= mean_absolute_error(y_test, ypred)
    rmse= mean_squared_error(y_test, ypred) ** 0.5
    r2= r2_score(y_test, ypred)
    result.append((name, alpha if alpha else "-", mae, rmse, r2))

result_df= pd.DataFrame(result)
print(result_df)