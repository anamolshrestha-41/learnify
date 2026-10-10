## Task 3:
build:
Model 1
Linear Regression
Model 2
Polynomial Regression
degree = 2
Model 3
Polynomial Regression
degree = 3
Model 4
Polynomial Regression
degree = 5

For every model calculate:

MAE
RMSE
R²

Create a table:

| Model | Degree | MAE | RMSE | R² |
|-------|--------|-----|------|----|
| Linear | 1 | ... | ... | ... |
| Polynomial | 2 | ... | ... | ... |
| Polynomial | 3 | ... | ... | ... |
| Polynomial | 5 | ... | ... | ... |

Then compare training RMSE vs testing RMS

## TASK - 4 : Regularization

Practice Task — Ridge Regression

Step 1
Create:
X = df[    [        "hours_studied",        "attendance",        "previous_score"    ]]y = df["final_score"]


Step 2
Split:
train_test_split(    X,    y,    test_size=0.2,    random_state=42)


Step 3
Train:
LinearRegression
Ridge(alpha=0.01)
Ridge(alpha=0.1)
Ridge(alpha=1)
Ridge(alpha=10)
Ridge(alpha=100)

Step 4
For every model calculate:
MAE
RMSE
R²

Step 5
Print coefficients.
Step 6
Create a table:
Model	Alpha	MAE	RMSE	R²
Linear	—			
Ridge	0.01			
Ridge	0.1			
Ridge	1			
Ridge	10			
Ridge	100			


Step 7
Answer:
1. Which alpha produced the lowest RMSE?
2. Which alpha produced the highest R²?
3. How did the coefficients change as alpha increased?
4. Did strong regularization improve or hurt performance?
5. Which model would you choose and why?