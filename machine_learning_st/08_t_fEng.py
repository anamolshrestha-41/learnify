import pandas as pd
import numpy as np
df = pd.DataFrame({
    "player": ["Ali", "Sam", "Raj", "Leo"],
    "minutes_played": [90, 45, 60, 0],
    "shots": [6, 2, 4, 0],
    "goals": [2, 1, 1, 0],
    "passes_completed": [36, 18, 24, 10],
    "passes_attempted": [40, 20, 30, 10]
})
print(df)
df["shots_per_90"]=(df["shots"]/df["minutes_played"]*90).replace([np.inf, -np.inf], np.nan) #replace np.infinity to np.nan
df["pass_completion_pct"]=(df["passes_completed"]/df["passes_attempted"].replace(0, np.nan))
df["shot_conversion_pct"]=(
    df["goals"]/df["shots"].replace(0,np.nan)*100
)
print(df.round(2).to_string())