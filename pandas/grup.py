import pandas as pd
#suppose: Supermarket, Instead of claculating total sales manually, Pandas groups rows
sales= pd.DataFrame({
   "City": ["Kathmandu", "Pokhara", "Kathmandu", "Butwal", "Pokhara"],
    "Sales": [100, 120, 140, 202, 301]
})

#Group rows
print(sales.groupby("City")["Sales"].sum()) #Removes duplicates and sorted in ascending order 

#agg() : Do multiple calculations together.
print(sales.groupby("City").agg({
    "Sales":["sum", "mean"]
}))

#transform() : Returns result for every row. Just like agg
sales["Maximum"]= sales.groupby("City")["Sales"].transform("max")
print(sales)

#filter(): keeps groups satisfying a condition.
print(sales.groupby("City").filter(lambda x: len(x)>=2)) #Only cities with at least two records remain.
print(sales.groupby("City").filter(lambda x: x["Sales"].sum()>250)) 

