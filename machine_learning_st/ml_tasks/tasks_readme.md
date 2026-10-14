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
   
## task: 5
1. Train Linear Regression, Ridge (alpha=1) and Lasso (alpha=0.1).
2. Use StandardScaler in the Ridge and Lasso Pipelines.
3. Calculate MAE, RMSE and R² for each model.
4. Print the Ridge and Lasso coefficients.
5. Try Lasso with alpha=0.001, 0.01, 0.1, 1 and 10.
6. Record how many coefficients become zero at each alpha.
Create a comparison table:
Model	Alpha	MAE	RMSE	R²	Zero coefficients
Linear Regression	—				0
Ridge	1				
Lasso	0.01				
Lasso	0.1				
Lasso	1 


## TASK 6:
Practice task
Train Ridge, Lasso and Elastic Net on the same training split.
1. Use StandardScaler inside each Pipeline.
2. Try multiple alpha values.
3. For Elastic Net, try l1_ratio values of 0.2, 0.5 and 0.8.
4. Record MAE, RMSE, R² and the number of zero coefficients.
5. Identify the best validation configuration.
6. Explain why it performed better than the alternatives.