import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(
    "postgresql+psycopg2://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)


import pandas as pd
from src.database import engine

query = """
SELECT
    p.player_name,
    p.position,
    COUNT(s.match_id) AS matches_played,
    SUM(s.goals) AS total_goals,
    SUM(s.assists) AS total_assists,
    AVG(s.minutes_played) AS average_minutes
FROM players p
LEFT JOIN player_match_stats s
    ON p.player_id = s.player_id
GROUP BY p.player_id, p.player_name, p.position;
"""

df = pd.read_sql(query, engine)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())


import matplotlib.pyplot as plt

df_sorted = df.sort_values(
    "total_goals",
    ascending=False
)

plt.figure(figsize=(10, 5))

plt.bar(
    df_sorted["player_name"],
    df_sorted["total_goals"]
)

plt.title("Total Goals by Player")
plt.xlabel("Player")
plt.ylabel("Total Goals")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("outputs/charts/player_goals.png")
plt.show()