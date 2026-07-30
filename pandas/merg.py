import pandas as pd

orders= pd.DataFrame({
    "CustomerID":[101,102,101],
    "ProductID":["P1","P2","P3"]
})
customers = pd.DataFrame({
    "CustomerID":[101,102],
    "CustomerName":["Ram","Hari"]
})
products= pd.DataFrame({
    "ProductID": ["P1", "P2", "P3"],
    "ProductName": ["Mouse", "Keyboard", "Monitor"],
    "Price": [700, 1200, 18000]
})

#merge(): Works like SQL JOIN.n :pd.merge(left_df, right_df, on="CommonColumn")
print(pd.merge(orders, customers, on="CustomerID"))
print(pd.merge(orders, products, on="ProductID"))

#JOIN: customer.join(address) :Mostly useful after setting index.
#Inner Join: Only matching rows
#Left Join: Keep all rows from left
#Right Join: Keep all right table rows
# Outer Join: Kepp everything, missing values beccomes NaN

#QN: Set CustomerID as index in both tables and use join()

orders=orders.set_index("CustomerID")
customers= customers.set_index("CustomerID")
print(orders.join(customers))

#concat(): Stacks DatFrames
print(pd.concat([orders, products]))