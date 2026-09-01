"""
Problem: Penguin Species Explorer Project (DATAS04)
Platform: CodeChef
Link: https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ01/problems/DATAS04
Date Solved: 2026-09-01
Difficulty: Medium
Topics: Seaborn, Matplotlib, Data Visualization, Scatter Plot, Box Plot, EDA

Approach:
Load and clean the seaborn "penguins" dataset (drop NaNs), then produce two
exploratory visualizations: a scatter plot of bill length vs. bill depth
colored by species, and a box plot of body mass distribution grouped by
species. Both plots are saved as PNGs for offline review (headless Agg backend).

Time Complexity:  O(n) — single pass to clean data, plotting is linear in
                   the number of rows (n = penguin records, ~333 after dropna).
Space Complexity: O(n) — one cleaned DataFrame held in memory; no extra
                   data structures beyond the plot objects.
"""


# ---------------------------- Solution ---------------------------------


import seaborn as sns

import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt

# TODO: 1. Set the theme to "whitegrid" for better styling
sns.set_theme(style="whitegrid")


# 1. Load Penguin Dataset
def load_data():
    """
    Load the penguins dataset using seaborn and clean it.
    """
    # TODO: 2. Load the "penguins" dataset
    df = sns.load_dataset("penguins")

    # TODO: 3. Drop rows with missing values, this prevents errors during plotting
    df = df.dropna()

    print("Dataset loaded and cleaned successfully!")

    if df is not None:
        print("\nSample Data (first 5 rows):")

        # display only relevant columns (species, bill_length_mm, bill_depth_mm, body_mass_g)
        print(df[["species", "bill_length_mm", "bill_depth_mm", "body_mass_g"]].head())

    return df


# 2. Scatter Plot: Bill Length vs Bill Depth
def plot_bill_comparison(df):
    """
    Create a scatter plot comparing bill length and bill depth by species.
    """
    # TODO: 4. Set the figure size to (8, 6)
    plt.figure(figsize=(8, 6))

    # TODO: 5. Create a scatterplot
    # Arguments: data=df, x="bill_length_mm", y="bill_depth_mm", hue="species"
    # Styling: palette="deep", s=100
    sns.scatterplot(
        data=df,
        x="bill_length_mm",
        y="bill_depth_mm",
        hue="species",
        palette="deep",
        s=100
    )

    # TODO: 6. Add Title and Axis Labels
    # Title: "Bill Length vs Bill Depth by Penguin Species"
    # X-label: "Bill Length (mm)", Y-label: "Bill Depth (mm)"
    plt.title("Bill Length vs Bill Depth by Penguin Species")
    plt.xlabel("Bill Length (mm)")
    plt.ylabel("Bill Depth (mm)")

    # TODO: 7. Save the plot as "bill_comparison.png"
    filename = "bill_comparison.png"
    plt.savefig(filename)

    print(f"Scatter plot saved as: {filename}")


# 3. Box Plot: Body Mass Distribution
def plot_body_mass_distribution(df):
    """
    Create a box plot showing body mass distribution across species.
    """
    # TODO: 8. Set the figure size to (8, 6)
    plt.figure(figsize=(8, 6))

    # TODO: 9. Create a boxplot
    # Arguments: data=df, x="species", y="body_mass_g", hue="species"
    # Styling: palette="Set2", legend=False
    sns.boxplot(
        data=df,
        x="species",
        y="body_mass_g",
        hue="species",
        palette="Set2",
        legend=False
    )

    # TODO: 10. Add Title and Axis Labels
    # Title: "Body Mass Distribution by Penguin Species"
    # X-label: "Species", Y-label: "Body Mass (g)"
    plt.title("Body Mass Distribution by Penguin Species")
    plt.xlabel("Species")
    plt.ylabel("Body Mass (g)")

    # TODO: 11. Save the plot as "body_mass_distribution.png"
    filename = "body_mass_distribution.png"
    plt.savefig(filename)

    print(f"Box plot saved as: {filename}")


if __name__ == "__main__":
    print("Penguin Species Explorer Project\n")

    # Load Data
    df = load_data()

    # Generate Plots
    plot_bill_comparison(df)
    plot_body_mass_distribution(df)
