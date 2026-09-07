import pandas as pd

df= pd.DataFrame({
    "title": ["Movie A", "Movie B", "Movie C", "Movie D"],
    "country": ["USA", "Nepal", None, None],
    "price": [200, None, 400, 300]
})

print(df.isna().sum())
# print(df["country"].fillna("Indonesia", inplace=True))
print(df["country"].dropna())
missing_percentage= df.isna().mean()*100
print(missing_percentage)
print(df["price"].fillna(df["price"].isna().mean()+200))