import pandas as pd
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge, ElasticNet, Lasso
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

X= df[["hours_studied", "attendance", "previous_score"]]
y= df["final_score"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size= 0.2,
    random_state= 42
)

ridge= Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge())
])
ridge_parameters={
    "model__alpha": [0.01, 0.1, 1, 10, 100]
}
cv= KFold(
    n_splits=5,
    shuffle= True,
    random_state= 42
)
ridge_search= GridSearchCV(
    estimator= ridge,
    param_grid= ridge_parameters,
    scoring="neg_root_mean_squared_error",
    cv=cv,
    n_jobs= -1
)
ridge_search.fit(X_train, y_train)
print("Best Ridge Parameters:", ridge_search.best_params_)
print("Best CV RMSE: ", -ridge_search.best_score_)
best_ridge= ridge_search.best_estimator_
test_pred= best_ridge.predict(X_test)
print("Test MAE:", mean_absolute_error(y_test, test_pred))
print("Test RMSE:", mean_squared_error(y_test, test_pred)**0.5)
print("Test R2:", r2_score(y_test, test_pred))

elastic_pipeline= Pipeline([
    ("scaler", StandardScaler()),
    ("model", ElasticNet(max_iter=10000))
])
elastic_params = {
    "model__alpha": [0.001, 0.01, 0.1, 1, 10],
    "model__l1_ratio": [0.2, 0.5, 0.8, 1.0]
}

elastic_search = GridSearchCV(
    elastic_pipeline,
    param_grid=elastic_params,
    scoring="neg_root_mean_squared_error",
    cv=cv,
    n_jobs=-1
)

elastic_search.fit(X_train, y_train)

print("Best parameters:", elastic_search.best_params_)
print("Best CV RMSE:", -elastic_search.best_score_)

searches = {
    "Ridge": (
        Pipeline([
            ("scaler", StandardScaler()),
            ("model", Ridge())
        ]),
        {"model__alpha": [0.01, 0.1, 1, 10, 100]}
    ),

    "Lasso": (
        Pipeline([
            ("scaler", StandardScaler()),
            ("model", Lasso(max_iter=10000))
        ]),
        {"model__alpha": [0.001, 0.01, 0.1, 1, 10]}
    ),

    "Elastic Net": (
        Pipeline([
            ("scaler", StandardScaler()),
            ("model", ElasticNet(max_iter=10000))
        ]),
        {
            "model__alpha": [0.001, 0.01, 0.1, 1, 10],
            "model__l1_ratio": [0.2, 0.5, 0.8, 1.0]
        }
    )
}

results = []

for name, (pipeline, params) in searches.items():
    search = GridSearchCV(
        pipeline,
        param_grid=params,
        scoring="neg_root_mean_squared_error",
        cv=cv,
        n_jobs=-1
    )

    search.fit(X_train, y_train)
    pred = search.predict(X_test)

    results.append({
        "Model": name,
        "Best Parameters": search.best_params_,
        "CV RMSE": -search.best_score_,
        "Test MAE": mean_absolute_error(y_test, pred),
        "Test RMSE": mean_squared_error(y_test, pred) ** 0.5,
        "Test R²": r2_score(y_test, pred)
    })

results_df = pd.DataFrame(results)

print(
    results_df.sort_values("CV RMSE").to_string(index=False)
)