import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
df= pd.DataFrame({
     "annual_income": [
        20, 22, 25, 28,
        50, 52, 55, 58,
        80, 85, 90, 95
    ],
    "spending_score": [
        15, 20, 18, 25,
        45, 50, 48, 55,
        80, 85, 90, 88
    ]
})
scaler= StandardScaler()
X_scaled=scaler.fit_transform(df)

model=AgglomerativeClustering(
    n_clusters=3,
    linkage="ward" #Merge groups in a way that tries to keep points within each group close together.
)
model.fit(X_scaled)
df["cluster"]=model.fit_predict(X_scaled)
print(df)
plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    s=100
)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Hierarchical Clustering")
plt.show()
#Dendogram:
linked=linkage(X_scaled, method="ward")
plt.figure(figsize=(10, 5))
dendrogram(linked)

plt.title("Customer Clustering Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Distance")
plt.show()

## TASK:
clust=[2,3,4]
for c in clust:
    model=AgglomerativeClustering(
        n_clusters=c,
        linkage="ward"
    )
    df["clust"]=model.fit_predict(X_scaled)
    print(df)
    plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    s=100
    )
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Hierarchical Clustering")
    plt.show()
    link= linkage(X_scaled, method="ward")
    plt.figure(figsize=(8,4))
    dendrogram(link)
    plt.xlabel("Customer")
    plt.xlabel("Distance")
    plt.title("Customer Clustering Dendogram")
    plt.show()