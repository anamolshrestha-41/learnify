import os
import pandas as pd

def exportReport(summary, monthlySales, regionSales, customerSummary, segmentSummary, bestProducts, categorySales, regionCategorySales):
    os.makedirs("outputs", exist_ok=True)

    #Export CSV files
    summary.to_csv("outputs/summary.csv", index=False)

    monthlySales.to_csv("outputs/monthlySales.csv", index=False)

    regionSales.to_csv("output/regionSales.csv")

    segmentSummary.to_csv(
        "outputs/segmentSummary.csv",
        index=False
    )

    bestProducts.to_csv(
        "outputs/bestProducts.csv",
        index=False
    )

    categorySales.to_csv(
        "outputs/categorySales.csv",
        index=False
    )

    regionCategorySales.to_csv(
        "outputs/regionCategorySales.csv"
    )

    #Export excel report

    with pd.ExcelWriter(
        "outputs/final_retail_report.xlsx"
    ) as writer:

        summary.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

        monthlySales.to_excel(
            writer,
            sheet_name="Monthly Sales",
            index=False
        )

        regionSales.to_excel(
            writer,
            sheet_name="Region Sales",
            index=False
        )

        customerSummary.to_excel(
            writer,
            sheet_name="Customers",
            index=False
        )

        segmentSummary.to_excel(
            writer,
            sheet_name="Segments",
            index=False
        )

        bestProducts.to_excel(
            writer,
            sheet_name="Best Products",
            index=False
        )

        categorySales.to_excel(
            writer,
            sheet_name="Categories",
            index=False
        )

        regionCategorySales.to_excel(
            writer,
            sheet_name="Region Category"
        )
