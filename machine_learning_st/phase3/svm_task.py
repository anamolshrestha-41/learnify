from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

iris=load_iris(as_frame=True)
df=iris.frame
X=df.drop(columns="target")
y=df["target"]

X_train, X_test, y_train, y_test= train_test_split(
    X,
    y,
    stratify=y,
    test_size=0.2,
    random_state=42
)
for kernel in ["linear", "rbf"]:
    model=Pipeline([
        ("scaler", StandardScaler()),
        ("svm", SVC(
           kernel=kernel,
           C=1.0,
           gamma="scale" 
        ))
    ])
    model.fit(X_train, y_train)
    y_pred=model.predict(X_test)
    print(f"Training Accuracy: {model.score(X_train, y_train)}")
    print(f"Testing Accuracy: {model.score(X_test, y_test)}")

for C in [0.1, 1, 100]:
    for g in [0.1, 10]:
        model=Pipeline([
            ("scaler", StandardScaler()),
            ("svm", SVC(
                kernel="rbf",
                C=C,
                gamma=g
            ))
        ])
        model.fit(X_train, y_train)
        y_pred=model.predict(X_test)
        print(f"Accuracy Score: {accuracy_score(y_test, y_pred)}")
        print(f"Classification Report: {classification_report(y_test, y_pred, target_names=iris.target_names )}")