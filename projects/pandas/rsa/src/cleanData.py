import pandas as pd

def cleanData(orders, customers, products):
    #Convert order date to date time
    orders["OrderDate"]=pd.to_datetime(
        orders["OrderDate"]
    )

    #Remove duplicate rows
    orders=orders.drop_duplicates()
    customers= customers.drop_duplicates()
    products= products.drop_duplicates()

    #Remove invalid dates
    orders= orders.dropna(subset=["OrderDate"])

    #Remove invalid quantities
    orders= orders[orders["Quantity"]>0]

    #Remove invalid product prices
    products= products[products["Price"]>0]

    #Remove rows with missing IDs
    orders= orders.dropna(subset=["OrderID", "CustomerID", "ProductID"])
    customers=customers.dropna(subset=["CustomerID"])
    products=products.dropna(subset=["ProductID"])

    #Convert IDs to string
    orders["CustomerID"]=orders["CustomerID"].astype(str)
    orders["ProductID"]= orders["ProductID"].astype(str)

    customers["CustomerID"]= customers["CustomerID"].astype(str)
    products["ProductID"]= products["ProductID"].astype(str)

    return orders, customers, products