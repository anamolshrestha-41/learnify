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