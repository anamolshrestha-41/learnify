import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
df=pd.DataFrame({
     "court_x": [
        2, 3, 4, 3,
        18, 19, 20, 19,
        9, 10, 11, 10,
        1, 20
    ],
    "court_y": [
        2, 3, 2, 4,
        18, 19, 18, 20,
        9, 10, 9, 11,
        18, 2
    ]
})
print(df)

scaler=StandardScaler()
X_scaled=scaler.fit_transform(df)


model=DBSCAN(
    eps=0.5,
    min_samples=3
)
df["cluster"]=model.fit_predict(X_scaled)
print(df)

plt.figure(figsize=(8,6))
for cluster_id in sorted(df["cluster"].unique()):
    group=df[df["cluster"]==cluster_id]
    label="Noise" if cluster_id==-1 else f"Cluster {cluster_id}"
    plt.scatter(
        group["court_x"],
        group["court_y"],
        s=100,
        label=label
    )
plt.xlabel("Court X")
plt.ylabel("Court Y")
plt.title("DBSCAN: Fitsal Player Position Groups")
plt.legend()
plt.grid(True)
plt.show()

#TASK:
for eps in [0.3, 0.8]:
    for min_samples in [2, 4]:
        model=DBSCAN(
            eps=eps,
            min_samples=min_samples
        )
        df["cluster"]=model.fit_predict(X_scaled)
        print(df)
        plt.figure(figsize=(16,8))
        for cluster_id in sorted(df["cluster"].unique()):
            group= df[df["cluster"]==cluster_id]
            label= "Noise" if cluster_id==-1 else {f"Cluster {cluster_id}"}
            plt.scatter(
                group["court_x"],
                group["court_y"],
                s=100,
                label=label
            )
        plt.xlabel("Court X")
        plt.ylabel("Court Y")
        plt.title("DBSCAN: Fitsal Player Position Groups")
        plt.legend()
        plt.grid(True)
        plt.show()