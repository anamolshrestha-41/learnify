import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

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
plt.scatter(
    df["annual_income"],
    df["spending_score"]
)
plt.xlabel("Annual Income (thousands)")
plt.ylabel("Spending Score")
plt.title("Customer Data Before Clustering")
plt.show()

scaler= StandardScaler()
X_scaled=scaler.fit_transform(df)
inertias=[]
k_values=[2,3,4]
for k in k_values:
    model=KMeans(
        n_clusters=k,
        n_init=5,
        random_state=42
    )
    model.fit(X_scaled)
    df["cluster_num"]=model.labels_
    print(df)
    inertias.append(model.inertia_)
    centers=scaler.inverse_transform(model.cluster_centers_)
    cluster_df=pd.DataFrame(
        centers,
        columns=["annual_income", "spending_score"]
    )
    print(cluster_df)
    plt.scatter(df["annual_income"], df["spending_score"], c=df["cluster_num"])
    plt.title("Customer segmentation using KMeans")
    plt.xlabel("Annual Income (Thousand)")
    plt.ylabel("Spending Score")
    plt.show()

plt.plot(k_values, inertias, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()