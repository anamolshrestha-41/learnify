import matplotlib.pyplot as plt


def save_csv(df, filename):
    """
    Save a DataFrame as CSV.
    """
    df.to_csv(filename, index=False)
    print(f"Saved: {filename}")


def save_summary(text, filename="Player Summary.txt"):
    """
    Save text summary to a file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Saved: {filename}")


def save_plot(filename="plot.png"):
    """
    Save the current matplotlib figure.
    """
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    print(f"Saved: {filename}")