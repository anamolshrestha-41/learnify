## Begin Task
Practice task
1. Load student_pass.csv.
2. Use hours_studied and attendance as features.
3. Use passed as the target.
4. Split the dataset with test_size=0.3, random_state=42, and stratify=y.
5. Train LogisticRegression.
6. Print predictions and predicted probabilities.
7. Calculate accuracy and display the confusion matrix.
8. Predict the result for a student with 6 study hours and 80% attendance.
9. Explain the difference between predict() and predict_proba().
    
## Task 2
Practical task
Use your student_pass.csv dataset and trained Logistic Regression model.
1. Print the intercept and coefficients.
2. Calculate the odds ratio for each coefficient.
3. Get probabilities for the test data using predict_proba().
4. Create predictions at thresholds 0.3, 0.5, and 0.7.
5. Calculate accuracy, precision, and recall at each threshold.
6. Explain how changing the threshold affected the predictions.

## TASK 3:
7. Practical example: Predict flower species
We'll use the built-in Iris dataset. It contains measurements of flowers and three possible species.
Step 1 — Load the dataset
import pandas as pdfrom sklearn.datasets import load_irisiris = load_iris(as_frame=True)df = iris.frameprint(df.head())print(df["target"].value_counts())



The target column contains numbers representing the flower species:
- 0 = Setosa
- 1 = Versicolor
- 2 = Virginica
Step 2 — Separate features and target
X = df.drop(columns="target")y = df["target"]print("Features:", X.columns.tolist())print("Target classes:", y.unique())



X contains the flower measurements. y contains the species we want to predict.
Step 3 — Split the data
from sklearn.model_selection import train_test_splitX_train, X_test, y_train, y_test = train_test_split(    X,    y,    test_size=0.2,    random_state=42,    stratify=y)



- 80% of the data is used for training.
- 20% is held aside for testing.
- stratify=y helps keep the class proportions similar in both sets.
Step 4 — Train Logistic Regression
from sklearn.pipeline import make_pipelinefrom sklearn.preprocessing import StandardScalerfrom sklearn.linear_model import LogisticRegressionmodel = make_pipeline(    StandardScaler(),    LogisticRegression(max_iter=1000))model.fit(X_train, y_train)



The model learns from the training data. The scaler puts measurements on comparable scales before training.
Step 5 — Evaluate the model
from sklearn.metrics import accuracy_score, classification_reporty_pred = model.predict(X_test)print("Accuracy:", accuracy_score(y_test, y_pred))print(classification_report(    y_test,    y_pred,    target_names=iris.target_names,    zero_division=0))



The report shows how well the model predicts each flower species. We will study precision, recall, and F1-score properly in Phase 5: Model Evaluation.
Step 6 — Predict a new flower
new_flower = pd.DataFrame({    "sepal length (cm)": [5.1],    "sepal width (cm)": [3.5],    "petal length (cm)": [1.4],    "petal width (cm)": [0.2]})prediction = model.predict(new_flower)[0]probabilities = model.predict_proba(new_flower)[0]print("Predicted species:", iris.target_names[prediction])for species, probability in zip(    iris.target_names, probabilities):    print(f"{species}: {probability:.2%}")



The model returns the predicted species and its estimated probability for each of the three classes.
These probabilities are estimates from the model, not guarantees.

8. Your practice task
Use the Iris example above and complete these tasks yourself.
Practice checklist
0 of 6 completed
[ ] Train a Logistic Regression model using L2 regularization.
[ ] Train another model using L1 regularization.
[ ] Print the coefficients from both models.
[ ] Compare their test accuracy.
[ ] Predict the species of a new flower.
[ ] Print the predicted probabilities for all three species.


## TAsk 4:
Use the Iris dataset and complete these tasks:
- [ ] Train KNN with K = 3.
- [ ] Train KNN with K = 7.
- [ ] Compare their test accuracy.
- [ ] Predict the species of a new flower.
- [ ] Explain in your own words why scaling is important for KNN.
- [ ] Explain what could happen if K is too small.
  
## TAsk 5:
Your practice task
Using the Iris dataset:
- [ ] Train a Decision Tree with max_depth=2.
- [ ] Train another with max_depth=5.
- [ ] Compare training accuracy and test accuracy.
- [ ] Visualize both trees.
- [ ] Change criterion="gini" to criterion="entropy" and compare.
- [ ] Explain why a very deep tree can overfit.
  
## Task 6:
Your practice task
Use the Iris dataset and complete these tasks:
- [ ] Train a Random Forest with 50 trees.
- [ ] Train another with 200 trees.
- [ ] Compare training and test accuracy.
- [ ] Print the feature importances.
- [ ] Create a bar chart of feature importance.
- [ ] Predict a new flower and display its class probabilities.
- [ ] Explain why Random Forest uses different samples and features for its trees.
  

## Task 7: 
Your practice task
Use the Iris dataset and complete these tasks:
- [ ] Train SVM with kernel="linear".
- [ ] Train SVM with kernel="rbf".
- [ ] Compare their training and test accuracy.
- [ ] Try C=0.1, C=1, and C=100.
- [ ] For the RBF kernel, compare gamma="scale" with gamma=0.1 and gamma=10.
- [ ] Explain why feature scaling matters.
- [ ] Explain what support vectors and the margin mean in simple English.
  

## Task 8:
Your practice task
Using the Iris dataset:
- [ ] Train a GaussianNB model.
- [ ] Print training and test accuracy.
- [ ] Display the confusion matrix.
- [ ] Print predicted probabilities for three test examples.
- [ ] Compare its test accuracy with your Random Forest model.
- [ ] Explain why Naive Bayes is called “naive.”
- [ ] Explain the difference between GaussianNB and MultinomialNB.