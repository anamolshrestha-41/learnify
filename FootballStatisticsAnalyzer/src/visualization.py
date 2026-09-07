import matplotlib.pyplot as plt


def goal_histogram(df):
    """
    Plot a histogram of player goals.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(df["Goals"], bins=10, edgecolor="black")
    plt.title("Goals Histogram")
    plt.xlabel("Goals")
    plt.ylabel("Number of Players")
    plt.grid(axis="y", alpha=0.3)
    plt.show()


def top_players_chart(df):
    """
    Plot the Top 10 Goal Scorers.
    """
    top_players = df.nlargest(10, "Goals")

    plt.figure(figsize=(10, 6))
    plt.bar(top_players["Player"], top_players["Goals"])
    plt.title("Top 10 Goal Scorers")
    plt.xlabel("Player")
    plt.ylabel("Goals")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def age_distribution(df):
    """
    Plot the age distribution of players.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(df["Age"], bins=10, edgecolor="black")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Number of Players")
    plt.grid(axis="y", alpha=0.3)
    plt.show()


def country_chart(df):
    """
    Plot the distribution of players by country.
    """
    country_counts = df["Country"].value_counts()

    plt.figure(figsize=(10, 6))
    plt.bar(country_counts.index, country_counts.values)
    plt.title("Country Distribution")
    plt.xlabel("Country")
    plt.ylabel("Number of Players")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def club_distribution(df):
    """
    Plot the distribution of players by club.
    """
    club_counts = df["Club"].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(club_counts.index, club_counts.values)
    plt.title("Club Distribution (Top 10)")
    plt.xlabel("Club")
    plt.ylabel("Number of Players")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def position_distribution(df):
    """
    Plot the distribution of players by position.
    """
    position_counts = df["Position"].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(position_counts.index, position_counts.values)
    plt.title("Position Distribution")
    plt.xlabel("Position")
    plt.ylabel("Number of Players")
    plt.tight_layout()
    plt.show()