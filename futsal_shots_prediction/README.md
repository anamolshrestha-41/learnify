# FutsalIQ 
### Futsal Goal Prediction Using Ensemble Machine Learning

## About
FutsalIQ is a machine learning project that predicts whether a futsal shot results in a goal using shot distance, shot angle, defensive pressure and goalkeeper distance.

## Machine Learning Models
- Logistic Regression
- Decision Tree
- Random Forest
- Voting Classifier
- AdaBoost
- Gradient Boosting
- XGBoost

## Technologies
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Balanced Accuracy
- Average Precision


## How to Run

1. Clone the repository.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Place the dataset in `data/`.
4. Run the Jupyter Notebook.
5. Execute `src/predict.py` after training and saving the model.

## Results
See `outputs/reports/model_comparision.csv` for the model comparison.

## Limitations
Predictions depend on the quality and representativeness of the dataset. The model does not guarantee real-world goal outcomes.

## Future Work
- Real-time futsal shot prediction
- Player performance analytics
- Shot location visualization
- Interactive prediction dashboard

## Author
Anamol Shrestha

