from loadData import loadData
from cleanData import cleanData

from analysis import(createSalesDataset, monthSalesAnalysis, regionSalesAnalysis, customerSegmentation, bestProductAnalysis, categorySalesAnalysis, regionCategoryAnalysis, customerSegmentationAnalysis, createSummary)

from exportReport import exportReport

def main():
    #load data
    orders,customers,products=(
        loadData()
    )
    print("Data loaded successfully")
    print(f"Orders: {orders.shape}")
    print(f"Customers: {customers.shape}")
    print(f"Products: {products.shape}")

    #clean data
    orders, customers, products=(
        cleanData(orders, customers, products))
    print("Data Cleaned Successfully")

    #Merge Datasets
    sales= createSalesDataset(
        orders, customers, products
    )
    print("Datasets merged successfully.")
    print(f"Final Dataset Shape: {sales.shape}")

    #monthly sales
    monthlySales=(
        monthSalesAnalysis(sales)
    )

    #region sales
    regionSales=(regionSalesAnalysis(sales))

    #Customer Segmentation
    customerSummary=(
        customerSegmentation(sales)
    )
    segmentSummary=(customerSegmentationAnalysis(customerSummary))

    #best products
    bestProducts=(bestProductAnalysis(sales))
    
    #category analysis
    categorySales=(categorySalesAnalysis(sales))

    #region category pivot table
    regionCategorySales=(regionCategoryAnalysis(sales))

    #Overall summary
    summary=createSummary(sales)

    #Export Reports

    exportReport(summary, monthlySales, regionSales, customerSummary, segmentSummary, bestProducts, categorySales, regionCategorySales)
    print("Report exported successfully")
    print("Check the output folder")

if __name__=="__main__":
    main()