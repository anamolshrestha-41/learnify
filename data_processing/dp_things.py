#SimpleImpute is a scikit-learn class used to handle missing data.
from sklearn.impute import SimpleImputer
import numpy as np

num= np.array([[20], [30], [np.nan], [50]])
imputer= SimpleImputer(strategy="mean")
new_num= imputer.fit_transform(num)
print(new_num)

# When to use

# For numerical data:

# median → often a good choice when outliers exist
# mean   → when distribution is reasonably normal

# For categorical data:

# most_frequent

X = [
    [20],
    [25],
    [30],
    [None],
    [40]
]
imputer= SimpleImputer(strategy="median")
x_new= imputer.fit_transform(X)
print(x_new)

#Encoding: ML models works with numerical datas
#OneHotEncoder
from sklearn.preprocessing import OneHotEncoder as ohe
x=[["ktm"], ["pokhara"], ["bhaktapur"], ["ktm"]]
encoder= ohe(sparse_output=False)
x_new= encoder.fit_transform(x)
print(x_new)
cities = [
    ["Kathmandu"],
    ["Pokhara"],
    ["Chitwan"],
    ["Kathmandu"]
]
new_cities= encoder.fit_transform(cities)
print(new_cities)

#OrdinalEncoder
from sklearn.preprocessing import OrdinalEncoder as oe
x=[["High School"], ["Bachelor"], ["Master"]]
encoder= oe(
        categories=[["High School", "Bachelor", "Master"]]
)
x_new=encoder.fit_transform(x)
print(x_new)

#scaling: puts features on comparable scales
#Most common method: StandardScaler
from sklearn.preprocessing import StandardScaler as ss
X_1 = [
    [18, 15000],
    [25, 30000],
    [35, 70000],
    [45, 100000]
]
scaler= ss()
new_x= scaler.fit_transform(X_1)
print(new_x)
#normalization: MinMaxScaler
from sklearn.preprocessing import MinMaxScaler as mms
nu=[[10], [20], [30], [40]]
scaler= mms()
new_nu= scaler.fit_transform(nu)
print(new_nu)

#Feature selection
from sklearn.feature_selection import  SelectKBest, f_regression
X = [
    [20, 50000, 2],
    [25, 60000, 4],
    [30, 75000, 6],
    [35, 90000, 8]
]

y = [52000, 62000, 78000, 95000]
selector= SelectKBest(
    score_func= f_regression,
    k=2
)
selected= selector.fit_transform(X, y)
print(selected)

#train-test_split
from sklearn.model_selection import train_test_split
X = [
    [20],
    [25],
    [30],
    [35],
    [40],
    [45],
    [50],
    [55],
    [60],
    [65]
]

y = [
    20000,
    25000,
    30000,
    35000,
    40000,
    45000,
    50000,
    55000,
    60000,
    65000
]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
print(X_train, X_test, y_train, y_test)

##pipeline
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

pipeline= Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", ss()),
    ("model", LinearRegression())
])
pipeline.fit(X_train, y_train)
predictions=pipeline.predict(X_test)
print(predictions)