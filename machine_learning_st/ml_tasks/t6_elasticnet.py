import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

datas={
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

df= pd.DataFrame(datas)
X=df[[
    "hours_studied",
    "attendance",
    "previous_score"
]]
y= df["final_score"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state= 42
)

results=[]

for alpha in [0.1, 1.0, 10.0]:
        models={
            "ridge": Pipeline([
                ("scaler", StandardScaler()),
                ("ridge", Ridge(alpha=alpha))
            ]),
            "lasso":Pipeline([
                ("scaler", StandardScaler()),
                ("lasso", Lasso(alpha=alpha))
            ]),
        }
        for name, model in models.items():
              model.fit(X_train, y_train)
              y_pred= model.predict(X_test)
              mae= mean_absolute_error(y_test, y_pred)
              rmse= mean_squared_error(y_test, y_pred)** 0.5
              r2= r2_score(y_test, y_pred)
              coefficients= model.named_steps[name].coef_
              results.append({
                  "alpha": alpha,
                  "l1_ratio": None,
                  "mae": mae,
                  "rmse": rmse,
                  "r2": r2,
                  "coefficients": coefficients
              })
for l1_ratio in [0.2, 0.5, 0.8]:
         model=Pipeline([
            ("scaler", StandardScaler()),
            ("elasticnet", ElasticNet(
                alpha=alpha,
                l1_ratio = l1_ratio,
                max_iter=10000
            ))
         ])

         model.fit(X_train, y_train)
         y_pred= model.predict(X_test)
         mae= mean_absolute_error(y_test, y_pred)
         rmse= mean_squared_error(y_test, y_pred)** 0.5
         r2= r2_score(y_test, y_pred)
         coefficients= model.named_steps["elasticnet"].coef_
         results.append({
            "alpha": alpha,
            "l1_ratio": l1_ratio,
            "mae": mae,
            "rmse": rmse,
            "r2": r2,
            "coefficients": coefficients
        })
results_df= pd.DataFrame(results)
print(results_df)