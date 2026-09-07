from loadData import load_data
from explore import explore_data
from cleanData import clean_data
from mergeData import merge_data
from playerAnalysis import top_players, player_summary
from teamAnalysis import country_statistics, club_statistics
from visualization import (
    plot_top_players,
    plot_country_statistics,
    plot_club_statistics,
)
from exportResult import save_csv, save_summary, save_plot


def main():
    # Load Data
    name, appearances, league, rating = load_data("../datas/all_player_profiles.csv", 
                                                   "../datas/all_player_stats.csv")

    # Explore
    explore_data(name, appearances, league, rating)

    # Clean
    name, appearances, league, rating = clean_data(
        name, appearances, league, rating
    )

    # Merge
    merged_df = merge_data(name, appearances, league, rating)

    # Player Analysis
    top_players_df = top_players(merged_df)
    summary = player_summary(top_players_df)

    # Team Analysis
    country_stats = country_statistics(merged_df)
    club_stats = club_statistics(merged_df)

    # Visualization
    plot_top_players(top_players_df)
    save_plot("Top Players.png")

    plot_country_statistics(country_stats)
    save_plot("Country Statistics.png")

    plot_club_statistics(club_stats)
    save_plot("Club Statistics.png")

    # Export
    save_csv(top_players_df, "Top Players.csv")
    save_csv(country_stats, "Country Statistics.csv")
    save_csv(club_stats, "Club Statistics.csv")
    save_summary(summary, "Player Summary.txt")


if __name__ == "__main__":
    main()