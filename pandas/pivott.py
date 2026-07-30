import pandas as pd

sales= pd.DataFrame({
    "City": ["Kathmandu", "Kathmandu", "Pokhara", "Pokhara"],
    "Product": ["Mouse", "Keyboard", "Mouse", "Keyboard"],
    "Sales": [100, 200, 300, 150]
})
#Change shape (pivot()) : limitation: pivot() cannot handle duplicates.
pivoted=sales.pivot(
    index="City",
    columns= "Product",
    values="Sales"
)
print(pivoted)

# pivot_table()
# Most used.
# Handles duplicates.
# Can calculate averages.
sales2 = pd.DataFrame({
    "City": ["Kathmandu", "Kathmandu", "Kathmandu", "Pokhara"],
    "Product": ["Mouse", "Mouse", "Keyboard", "Mouse"],
    "Sales": [100, 150, 200, 300]
})
pivoTable= sales2.pivot_table(
    values="Sales",
    index="City",
    columns="Product",
    aggfunc="mean"
)
print(pivoTable)

#melt() opposite of pivot
meltt=pd.melt(sales, id_vars="City")
print(meltt)