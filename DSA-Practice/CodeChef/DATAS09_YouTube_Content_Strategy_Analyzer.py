"""
Problem   : YouTube Content Strategy Analyzer Project (DATAS09)
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ02/problems/DATAS09
Date      : 2026-09-04
Difficulty: Medium
Topics    : Pandas, NumPy, Matplotlib, Data Visualization, EDA

Approach:
- Load YouTube video stats from CSV into a DataFrame.
- Scatter plot: Views (x) vs Likes (y), with marker size scaled by
  comment_count to visualize engagement depth in a single chart.
- Grouped bar chart: Likes vs Comments per video (side-by-side bars)
  to compare engagement metrics across titles.
- Both charts saved as PNG for offline reporting.

Complexity:
- Time  : O(n) — single pass over n rows for each plot (matplotlib
          rendering itself is O(n) in points/bars drawn).
- Space : O(n) — one DataFrame copy in memory, no auxiliary
          structures beyond plotting buffers.
"""


# ------------------------- Solution -----------------------------------


import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files
import matplotlib.pyplot as plt

# 1. Load Dataset
def load_data():
    """
    Load and return the YouTube dataset.
    """
    path = "youtube.csv"
    df = pd.read_csv(path)
    
    print("Dataset Preview:")
    print(df.head())
    return df


# 2. Scatter Plot: Views vs Likes
def plot_scatter(df):
    """
    Create a scatter plot comparing Views vs Likes.
    Marker size proportional to comment count + slight transparency.
    """
    # Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10, 6))

    # Create a scatter plot
    plt.scatter(
        df["views"],
        df["likes"],
        s=df["comment_count"] * 0.3,
        color="purple",
        alpha=0.5,
        edgecolors="black"
    )

    # Add Title, X-label, and Y-label
    plt.title("Views vs Likes (Size = Comment Count)")
    plt.xlabel("Views")
    plt.ylabel("Likes")

    # Enable grid with alpha=0.5
    plt.grid(alpha=0.5)

    # Set Axis Limits
    plt.xlim(0, df["views"].max() * 1.1)
    plt.ylim(0, df["likes"].max() * 1.1)

    # Save the plot as "scatter_plot.png"
    plt.savefig("scatter_plot.png")

    print("Chart saved: scatter_plot.png")


# 3. Side-by-Side Bar Chart
def bar_chart_side_by_side(df):
    """
    Compare Likes and Comments per video using side-by-side bars.
    """
    titles = df["title"]
    likes = df["likes"]
    comments = df["comment_count"]

    # We are creating an array of indices for the X-axis (0 to len(titles))
    x = np.arange(len(titles))

    # Width of the bars
    width = 0.35

    # Set figure size to 12 inches by 6 inches
    plt.figure(figsize=(12, 6))

    # Plot 'Likes' bars shifted to the LEFT with color = skyblue
    plt.bar(x - width / 2, likes, width, color="skyblue", label="Likes")

    # Plot 'Comments' bars shifted to the RIGHT with color = orange
    plt.bar(x + width / 2, comments, width, color="orange", label="Comments")

    # Add Title, X-label, and Y-label
    plt.title("Engagement Analysis: Likes vs Comments")
    plt.xlabel("Video Title")
    plt.ylabel("Count")

    # Set X-axis ticks to be the video titles, rotated vertically
    plt.xticks(x, titles, rotation=90)

    # Show Legend
    plt.legend()

    # Show grid with alpha=0.7 and only horizontal lines
    plt.grid(axis="y", alpha=0.7)

    # We are adjusting layout to prevent clipping of tick-labels
    plt.tight_layout()

    # Save the plot as "bar_chart.png"
    plt.savefig("bar_chart.png")

    print("Chart saved: bar_chart.png")


if __name__ == "__main__":
    print("YouTube Content Strategy Analyzer...\n")

    # Load Data
    df = load_data()

    if df is not None:
        # Scatter Plot: Views vs Likes
        plot_scatter(df)

        # Bar Chart: Likes vs Comments
        bar_chart_side_by_side(df)
