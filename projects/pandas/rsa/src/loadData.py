import pandas as pd

def loadData():
    orders= pd.read_csv("data/Orders.csv")
    products= pd.read_csv("data/Products.csv")
    customers= pd.read_csv("data/Customers.csv")

    return orders, products, customers