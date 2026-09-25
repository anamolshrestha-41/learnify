import pandas as pd
from sklearn.linear_model import LinearRegression

data={
    "hrs_studied": [1,2,3,4,5,6,7,8,9,10],
    "exam_score":[40, 50, 57, 63, 69, 72, 75, 80, 84, 89]
}

df= pd.DataFrame(data)

x=df[["hrs_studied"]]
y=df["exam_score"]

model= LinearRegression()
model.fit(x,y)
new_data = pd.DataFrame({
    "hrs_studied": [7]
})
prediction= model.predict(new_data)
print("Coeff: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("Predicted score: ", prediction[0])