import pandas as pd
import plotly.express as px

datas={
     "age": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 32, 35, 38, 40, 45, 50, 55],
    
    "duration": [10, 12, 15, 18, 20, 22, 25, 27, 30, 32,
                 35, 38, 40, 45, 50, 55, 60, 70, 90, 120],
    
    "income": [20000, 22000, 25000, 27000, 30000, 32000, 35000,
               37000, 40000, 42000, 45000, 48000, 50000, 55000,
               60000, 65000, 70000, 80000, 100000, 150000]
}
df= pd.DataFrame(datas)

#Three Features: age, duration, income
#For age
df['age'].describe()
print(f"Mean:{df['age'].mean()}")
print(f"Median:{df['age'].median()}")
print(f"Min:{df['age'].min()}")
print(f"Max:{df['age'].max()}")
print(f"Standard Deviation:{df['age'].std()}")
print(f"Skewness:{df['age'].skew()}")
fig= px.histogram(df['age'], x="age", title="Age distribution")
fig.show()
#For duration
df['duration'].describe()
print(f"Mean:{df['duration'].mean()}")
print(f"Median:{df['duration'].median()}")
print(f"Min:{df['duration'].min()}")
print(f"Max:{df['duration'].max()}")
print(f"Standard Deviation:{df['duration'].std()}")
print(f"Skewness:{df['duration'].skew()}")
fig= px.bar(df['duration'], x="duration", title="Income distribution")
fig.show()
#For income
df['income'].describe()
print(f"Mean:{df['income'].mean()}")
print(f"Median:{df['income'].median()}")
print(f"Min:{df['income'].min()}")
print(f"Max:{df['income'].max()}")
print(f"Standard Deviation:{df['income'].std()}")
print(f"Skewness:{df['income'].skew()}")
fig= px.scatter(df['income'], x="income", title="Income distribution")
fig.show()