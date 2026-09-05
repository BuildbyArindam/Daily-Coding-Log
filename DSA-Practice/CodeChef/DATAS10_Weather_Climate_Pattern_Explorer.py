"""
Problem: Weather & Climate Pattern Explorer Project
Platform: CodeChef
Link: https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ02/problems/DATAS10
Difficulty: Medium
Topics: Pandas (data loading/exploration), Seaborn, Data Visualization, Relational Plot (Scatter), KDE / Distribution Plot, Faceted Plot (displot/col facets)
Date Solved: 2026-09-05

Approach:
    Load a weather dataset with pandas, then explore temperature/humidity
    relationships across cities using Seaborn's figure-level plotting API:
    1. Relational scatter plot (temperature vs humidity, colored by city)
    2. KDE plot to view smoothed temperature distribution per city
    3. Faceted KDE plot (separate subplot per city) via displot(col="city")
    Each chart is rendered in headless mode (Agg backend) and saved as PNG.

Time Complexity:  O(n) — single pass over n rows per plotting call
                   (Seaborn/Matplotlib rendering cost is not counted as
                   algorithmic complexity)
Space Complexity: O(n) — dataframe held in memory; no extra structures
                   beyond what pandas/seaborn allocate internally
"""


# ---------------------- Solution --------------------------------


import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt

# 1. Load Dataset
def load_weather_data():
    """
    Load and return the weather dataset.
    """
    # Load dataset from "weather.csv"
    df = pd.read_csv("weather.csv")
    
    print("Dataset Preview:")
    
    # Show dataset first 5 rows
    print(df.head())

    return df


# 2. Scatter Plot: Temperature vs Humidity
def plot_temperature_vs_humidity(df):
    """
    Compare temperature vs humidity using a relational plot.
    """
    # Create a relational plot (scatter)
    g = sns.relplot(
        data=df,
        x="temperature",
        y="humidity",
        hue="city",
        kind="scatter"
    )

    # Add a Super Title (suptitle) to the Figure
    # Title: "Temperature vs Humidity"
    # Use y=1.02 to adjust vertical position
    g.fig.suptitle("Temperature vs Humidity", y=1.02)

    # Save the plot
    plt.savefig(
        "temp_vs_humid_scatter.png",
        bbox_inches="tight"
    )

    print("Chart saved: temp_vs_humid_scatter.png")


# 3. Distribution Chart: KDE Curve
def plot_temperature_kde(df):
    """
    Plot smooth temperature distributions.
    """
    # Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10, 6))

    
    # Create a KDE plot
    sns.kdeplot(
        data=df,
        x="temperature",
        hue="city",
        fill=True
    )

    # Add Title
    plt.title("Temperature Distribution (KDE)")

    # Add grid with transparency
    plt.grid(alpha=0.3)

    
    # Save plot
    plt.savefig("temperature_kde.png")


    print("Chart saved: temperature_kde.png")


# 4. Faceted Distribution Plot (Side-by-Side)
def plot_faceted_distribution(df):
    """
    Create separate charts for each city side-by-side.
    """
    # Create a faceted plot using sns.displot
    g = sns.displot(
        data=df,
        x="temperature",
        col="city",
        kind="kde",
        fill=True
    )

    # Add a Super Title
    # Use y=1.03 to adjust vertical position
    g.fig.suptitle("Faceted Temperature Distributions", y=1.03)

    
    # Save plot
    plt.savefig(
        "temperature_facets.png",
        bbox_inches="tight"
    )


    print("Chart saved: temperature_facets.png")


if __name__ == "__main__":
    print("Weather & Climate Pattern Explorer...\n")

    # 1. Load Data
    df = load_weather_data()

    if df is not None:
        # 2. Scatter Plot
        plot_temperature_vs_humidity(df)

        # 3. KDE Plot
        plot_temperature_kde(df)

        # 4. Faceted Plot
        plot_faceted_distribution(df)
