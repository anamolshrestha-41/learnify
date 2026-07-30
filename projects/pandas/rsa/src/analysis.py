import pandas as pd

def createSalesDataset(orders, customers, products):

    #Merge orders with customers
    sales= pd.merge(orders, products, on="ProductID", how="left")

    #Merge sales with products
    sales= pd.merge(sales, products, on="ProductID", how="left")

    #Calculate total sales
    sales["TotalSales"]=(sales["Quantity"]*sales["Price"])

    #Extract date information
    sales["Year"]= sales["OrderDate"].dt.year
    sales["Month"] = sales["OrderDate"].dt.to_period("ME")
    sales["MonthName"]= (sales["OrderDate"].dt.month_name())

    return sales

def monthSalesAnalysis(sales):
    monthlySales=(
        sales.groupby("Month").agg(
            TotalSales=("TotalSales", "sum"),
            TotalOrders=("OrderID", "nunique"),
            TotalQuantity=("Quantity", "sum")
        ).reset_index()
    )
    monthlySales["RollingAverage"]=(
        monthlySales["TotalSales"].cumsum()
    )

    return monthlySales

def regionSalesAnalysis(sales):
    regionSales=(
        sales.groupby("Region").agg(
            TotalSales=("TotalSales","sum"),
            TotalOrders=("OrdderID","nunique"),
            TotalQuantity=("Quantity", "sum"),
            AverageOrderValue=("TotalSales", "mean")
        ).sort_values(by="TotalSales", ascending=False).reset_index()
    )
    return regionSales

def customerSegmentation(sales):
    customerSummary=(
        sales.groupby([
            "CustomerID", "CustomerName"
        ]).agg(
            TotalSpent=("TotalSales", "sum"),
            TotalOrders=("OrderID", "nunique"),
            TotalQuantity=("Quantity", "sum")
        ).reset_index()
    )
    def segmentCustomer(row):
        if row["TotalSpent"]>=100000:
            return "Premium"
        elif row["TotalSpent"]>=50000:
            return "Regular"
        
        else: return "Basic"
    
    customerSummary=(
        customerSummary.sort_values(
            by="TotalSpent",
            ascending=False
        )
    )
    return customerSummary

def bestProductAnalysis(sales):
    bestProduct=(
        sales.groupby([
            "ProductID",
            "ProductName",
            "Category"
        ]).agg(
            TotalSales=("TotalSales", "sum"),
            TotalQuantity=("Quantity", "sum"),
            TotalOrder=("OrderID", "nunique")
        ).sort_values(
            by="TotalSales", ascending=False
        ).reset_index()
    )
    return bestProduct

def categorySalesAnalysis(sales):
    categorySales=(
        sales.groupby("Category").agg(
        TotalSales=("TotalSales", "sum"),
        TotalQuantity=("Quantity", "sum"),
        TotalOrders=("OrderID", "nunique")    
        ).sort_values(by="TotalSales", ascending=False).reset_index()
    )
    return categorySales

def regionCategoryAnalysis(sales):
    regionCategorySales=pd.pivot_table(
        sales, values="TotalSales", index="Region", columns="Category", aggfunc="sum", fill_value=0
    )
    return regionCategorySales

def customerSegmentationAnalysis(customerSummary):
    segmentSummary=(
        customerSummary.groupby("Segment").agg(
            TotalCustomers=("CustomerID", "count"),
            TotalRevenue=("TotalSpent", "sum"),
            AverageCustomerSpending=("TotalSpent", "mean")
        ).reset_index()
    )
    return segmentSummary

def createSummary(sales):
    totalRevenue= sales["TotalSales"].sum()
    totalOrders= sales["OrderID"].nunique()
    totalCustomers= sales["CustomerID"].nunique()
    totalProducts= sales["ProductID"].nunique()

    averageOrderValue=(
        totalRevenue/totalOrders
    )

    summary= pd.DataFrame({
        "Metric":[
            "Total Revenue",
            "Total Orders",
            "Total Customers",
            "Total Products",
            "Average Order Value"
        ],
        "Value":[
            totalRevenue,
            totalOrders,
            totalCustomers,
            totalProducts,
            averageOrderValue
        ]
    })
    return summary
