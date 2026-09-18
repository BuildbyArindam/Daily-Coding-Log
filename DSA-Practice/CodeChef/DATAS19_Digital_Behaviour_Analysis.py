"""
Problem   : Digital Behaviour Analysis Project (DATAS19)
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ04/problems/DATAS19
Date      : 2026-09-18
Difficulty: Medium
Topics    : Pandas, Matplotlib, Data Visualization, Time Series, EDA

Approach:
    - Load daily digital-behaviour CSV, parse Date to datetime, sort chronologically.
    - Build a 1x2 subplot figure:
        1) Line plot of ScreenTime vs AppUsage over time, with a reference
           horizontal line at the daily usage limit.
        2) Scatter plot of Unlocks vs ScreenTime, colored by AppUsage
           (colormap = viridis) to expose a 3-variable correlation.
    - Save combined figure to disk as a single PNG.

Complexity:
    Time  : O(n log n) — dominated by the sort_values() on Date;
            plotting itself is O(n).
    Space : O(n) — one DataFrame copy held in memory for the full dataset.
"""


# ----------------------------- Solution ---------------------------------------


import pandas as pd

import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files

import matplotlib.pyplot as plt

# Constants
FILE_NAME = "digital_behaviour.csv"
DAILY_LIMIT = 6.0


def load_data(filename):
    """
    Load data and convert Date column.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filename)

        # Convert the 'Date' column to datetime objects
        df['Date'] = pd.to_datetime(df['Date'])

        # Sort the DataFrame by 'Date' and return the sorted DataFrame
        return df.sort_values(by='Date')

    except FileNotFoundError:
        print("Error: File not found.")
        return pd.DataFrame()


def visualize_digital_behavior(df):
    """
    Create a side-by-side plot layout.
    """

    # 1. Setup Subplots in 1 Row and 2 Columns
    # Set the figure size to 15 inches by 5 inches
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Assigning axes to variables for easier use
    ax1 = axes[0]  # Axis for Plot 1
    ax2 = axes[1]  # Axis for Plot 2

    # Add a main title for the entire figure
    fig.suptitle("Project 3: Digital Behaviour Analysis")

    # === PLOT 1: Daily Trends (Line Plot) ===

    # Plot 'Date' on X-axis and 'ScreenTime' on Y-axis
    # Add label 'Screen Time'
    ax1.plot(df['Date'], df['ScreenTime'], label='Screen Time')

    # Plot another line for 'AppUsage'
    # Make this line dashed and add label 'App Usage'
    ax1.plot(
        df['Date'],
        df['AppUsage'],
        linestyle='--',
        label='App Usage'
    )

    # Add a horizontal line for the daily limit
    ax1.axhline(
        y=DAILY_LIMIT,
        color='red',
        linestyle='--',
        label='Daily Limit'
    )

    # Add a title to ax1
    ax1.set_title("Daily Usage Trends")

    # Add X axis label and Y axis label
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Hours")

    # Add a legend
    ax1.legend()

    # Rotate date labels by 45 degrees
    ax1.tick_params(axis='x', rotation=45)

    # === PLOT 2: Correlations (Scatter with Color Map) ===

    # Create a scatter plot
    scatter = ax2.scatter(
        df['Unlocks'],
        df['ScreenTime'],
        c=df['AppUsage'],
        cmap='viridis',
        alpha=0.7
    )

    # Add title
    ax2.set_title("Unlocks vs. Screen Time")

    # Add X axis label and Y axis label
    ax2.set_xlabel("Unlocks")
    ax2.set_ylabel("Screen Time")

    # Add a Colorbar
    colorbar = fig.colorbar(scatter, ax=ax2)
    colorbar.set_label("App Usage (Hours)")

    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig("digital_behaviour_analysis.png")

    print("Plot saved as 'digital_behaviour_analysis.png'")


if __name__ == "__main__":
    df = load_data(FILE_NAME)

    if not df.empty:
        visualize_digital_behavior(df)
