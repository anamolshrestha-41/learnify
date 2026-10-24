from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestRegressor

iris=load_iris(as_frame=True)
df=iris.frame
X=df.drop(columns="target")
y=df["target"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
model=GaussianNB()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
print(f"Training Accurac: {model.score(X_train, y_train)}")
print(f"Testing Accuracy: {model.score(X_test, y_test)}")
print(f"Confusion Matrix:{confusion_matrix(y_test, y_pred)}")
print(f"Predicted Probabilities: {model.predict_proba(X_test[:3])}")
random_model=RandomForestRegressor(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
random_model.fit(X_train, y_train)
print(f"Test Accuracy of Random Forest: {random_model.score(X_test, y_test)}")
print(f"Test Accuracy of Navie Bayes: {model.score(X_test, y_test)}")