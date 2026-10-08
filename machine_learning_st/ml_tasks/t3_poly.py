import pandas as pd

datas={
     "hours_studied": [
        1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6,
        6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11,
        11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 16, 17
    ],
    "final_score": [
        35, 38, 42, 45, 47, 50, 52, 55, 57, 60,
        62, 65, 67, 70, 72, 75, 77, 80, 82, 84,
        86, 88, 89, 91, 92, 94, 95, 96, 98, 99
    ]
}
df= pd.DataFrame(datas)

X= df[["hours_studied"]]
y= df["final_score"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

result=[]

for degree in [1, 2, 3, 5]:
    model= Pipeline([
        ("polynomial",PolynomialFeatures( degree=degree, include_bias=False)),
        ("regression", LinearRegression())
    ])

    # training
    model.fit(X_train, y_train)
    #predict

    y_train_pred= model.predict(X_train)
    y_test_pred= model.predict(X_test)

    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    #train RMSE
    train_mse= mean_squared_error(y_train, y_train_pred)
    train_rmse= train_mse ** 0.5
    
    mae= mean_absolute_error(y_test, y_test_pred)
    test_mse= mean_squared_error(y_test, y_test_pred)
    test_rmse= test_mse ** 0.5
    r2score= r2_score(y_test, y_test_pred)

    result.append({
         "Model": "Linear" if degree == 1 else "Polynomial",
        "Degree": degree,
        "MAE": mae,
        "RMSE": test_rmse,
        "R²": r2score,
        "Train RMSE": train_rmse,
        "Test RMSE": test_rmse
    })

results_df=pd.DataFrame(result)
print(results_df)
#in order to see full results
print(results_df.to_string(index=False))