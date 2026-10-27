import pandas as pd
import os
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN

os.makedirs("outputs/plots", exist_ok=True)
df=pd.read_csv("./data/player_positions.csv")
X=df[["court_x","court_y"]]

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

kModel=KMeans(
    n_clusters=3,
    n_init=10,
    random_state=42
)
df["kmeans"]=kModel.fit_predict(X_scaled)
hModel=AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)
df["hierarchy"]=hModel.fit_predict(X_scaled)
dModel= DBSCAN(
    eps=0.6,
    min_samples=3
)
df["dbscan"]=dModel.fit_predict(X_scaled)

algorithms=["kmeans", "hierarchy", "dbscan"]

fig,axes=plt.subplots(1,3,figsize=(15,5))

for ax, algorithm in zip(axes, algorithms):
    scatter= ax.scatter(
        df["court_x"],
        df["court_y"],
        c=df[algorithm],
        s=100
    )
    ax.set_title(algorithm.capitalize())
    ax.set_xlabel("Court X")
    ax.set_ylabel("Court Y")
    ax.grid(True)
plt.savefig("outputs/plots/clustering_comparision.png", dpi=150)
plt.show()
plt.close()

df.to_csv("outputs/player_clusters.csv", index=False)