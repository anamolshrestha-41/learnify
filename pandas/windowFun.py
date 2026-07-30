import pandas as pd

#Suppose  Sales:
sales=pd.DataFrame({
    "Sales": [100, 150, 200, 300]
})
cunSum= sales["Sales"].cumsum()
print(cunSum) #output: 100, 250, 450, 750

#rolling(): Moving Average
rol= sales["Sales"].rolling(3).mean()
print(rol) #output: NaN NaN 150.000000 216.666667

#expanding(): Average from first row until current row
exp= sales["Sales"].expanding().mean()
print(exp) #output: 100.0 125.0 150.0 187.5

roll=sales["Sales"].rolling(2).mean()
print(roll.cumsum()) #NaN 125.0 300.0 550.0