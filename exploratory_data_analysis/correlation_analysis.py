import pandas as pd
import plotly.express as px
import numpy as np
data={
     "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Assignments": [50, 55, 65, 70, 75, 85, 90, 95],
    "Sleep_Hours": [8, 7, 7, 6, 6, 6, 5, 5],
    "Score": [45, 50, 58, 65, 70, 78, 85, 92]
}
df= pd.DataFrame(data)
corr= df.corr(numeric_only=True)
print(corr)
#corr matrix visulaization
# fig= px.density_heatmap(corr, title="Correlation Matrix")
# fig.show()

#Remove diagonal and duplicate correlations
corr_pairs= corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool)).stack().sort_values()
print(corr_pairs.head(1))
print(corr_pairs.tail(1))

#weak relationships
weak= corr_pairs[abs(corr_pairs)<0.3]
print(weak)

#potentially redundant features
redundant= corr_pairs[abs(corr_pairs)>0.8]
print(redundant)
