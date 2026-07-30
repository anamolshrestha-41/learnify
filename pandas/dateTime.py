import pandas as pd

# Almost every dataset contains dates.
# 2025-05-21
# Pandas can understand dates.

df = pd.DataFrame({
    "Date": ["2025-01-15", "2025-02-20", "2025-03-10"],
    "Sales": [100, 200, 150]
})
print(df)
# df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = pd.to_datetime(df["Date"])
print(df["Date"].dt.year) #year extraction
print(df["Date"].dt.month)  #month extraction
print(df["Date"].dt.day) #day extraction
print(df["Date"].dt.day_name()) #weekday extraction

# Resampling changes the frequency of time-series data.
# Convert daily stock prices into monthly average prices.

data={
    "Date": [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-02-01",
        "2024-02-02"
    ],
    "Price": [100, 102, 101, 110, 112]
}
resamData= pd.DataFrame(data)
resamData["Date"]= pd.to_datetime(resamData["Date"]) #date colum to datetime conversion
resamData.set_index("Date", inplace=True)
print(resamData)
monthlyAverage= resamData.resample("ME").mean()
print(monthlyAverage)

#Given date: 2024-12-25
date= pd.to_datetime("2024-12-25")
print(date.year)
print(date.month)
print(date.day)
print(date.day_name())
 #from dataframe
dataF=pd.DataFrame({
  "Date": ["2024-12-25", "2025-01-01", "2025-03-15"]
})
dataF["Date"]= pd.to_datetime(dataF["Date"])
dataF["Year"]= dataF["Date"].dt.year
print(dataF)