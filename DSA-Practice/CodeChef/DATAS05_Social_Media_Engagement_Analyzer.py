"""
Problem   : Social Media Engagement Analyzer Project (DATAS05)
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ01/problems/DATAS05
Difficulty: Medium
Date      : 2026-09-02
Topics    : Pandas, Matplotlib, Seaborn, Data Visualization,
            Stacked Bar Chart, Bubble Chart, DataFrame.melt(), Box Plot

Approach:
    - Load engagement data (likes/comments/shares) into a DataFrame.
    - Derive a `total_engagement` column via row-wise sum.
    - Visualize composition per post as a 3-layer stacked bar chart
      (likes -> comments -> shares, using `bottom=` for stacking).
    - Visualize the likes-vs-comments relationship as a bubble chart,
      encoding `shares` as marker size via seaborn's `size=` param.
    - Reshape wide -> long format with df.melt() and compare metric
      distributions using a Seaborn box plot.

Time Complexity : O(n) — single pass over n posts for aggregation;
                   plotting calls are O(n) as well (n is tiny here, n=8).
Space Complexity: O(n) — DataFrame + melted DataFrame copies, both linear in n.
"""


# -------------------------- Solution ---------------------------------


import pandas as pd
import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt
import seaborn as sns

# TODO: 1. Set the Seaborn theme to "whitegrid" for better styling
sns.set_theme(style="whitegrid")


# 1. Load Data
def load_data():
    """
    Create and return a Pandas DataFrame containing social media engagement data.
    """
    # We have pre-filled the data for you to save time!
    data = {
        "post_id": [1, 2, 3, 4, 5, 6, 7, 8],
        "likes": [120, 340, 560, 230, 410, 290, 600, 150],
        "comments": [30, 80, 120, 45, 95, 60, 150, 20],
        "shares": [15, 40, 75, 25, 60, 35, 100, 10]
    }

    # TODO: 2. Create a DataFrame from the dictionary above
    df = pd.DataFrame(data)

    print("Data loaded successfully!")

    # TODO: 3. Return the DataFrame
    return df


# 2. Compute Engagement
def analyze_engagement(df):
    """
    Calculate total engagement column.
    """
    # TODO: 4. Create a new column "total_engagement"
    # Formula: likes + comments + shares
    df["total_engagement"] = (
        df["likes"] + df["comments"] + df["shares"]
    )

    print("\nEngagement Summary (First 5 rows):")
    # We check if the column exists to avoid errors
    if "total_engagement" in df.columns:

        # TODO: 5. Print first 5 rows of post_id and total_engagement columns
        print(df[["post_id", "total_engagement"]].head())

    return df


# 3. Stacked Bar Chart (Matplotlib)
def plot_engagement_composition(df):
    """
    Visualize Likes, Comments, and Shares using a Stacked Bar Chart.
    """
    # TODO: 6. Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10, 6))

    # --- Layer 1: Likes (Base) ---
    # TODO: 7. Plot 'likes' vs 'post_id'
    # Label="Likes", Color="#3498db"
    plt.bar(
        df["post_id"],
        df["likes"],
        label="Likes",
        color="#3498db"
    )

    # --- Layer 2: Comments (Stacked on Likes) ---
    # TODO: 8. Plot 'comments' vs 'post_id'.
    # IMPORTANT: Use the parameter bottom=df["likes"] to stack it!
    # Label="Comments", Color="#e67e22"
    plt.bar(
        df["post_id"],
        df["comments"],
        bottom=df["likes"],
        label="Comments",
        color="#e67e22"
    )

    # --- Layer 3: Shares (Stacked on Likes + Comments) ---
    # TODO: 9. Calculate the new bottom (likes + comments)
    bottom_heights = df["likes"] + df["comments"]

    # TODO: 10. Plot 'shares' vs 'post_id' using bottom=bottom_heights
    # Label="Shares", Color="#2ecc71"
    plt.bar(
        df["post_id"],
        df["shares"],
        bottom=bottom_heights,
        label="Shares",
        color="#2ecc71"
    )

    # TODO: 11. Add title, labels, and legend
    # Title: "Engagement Composition per Post (Stacked)"
    plt.title("Engagement Composition per Post (Stacked)")
    plt.xlabel("Post ID")
    plt.ylabel("Count")
    plt.legend()

    filename = "engagement_composition.png"

    # TODO: Save the plot
    plt.savefig(filename)

    print(f"Chart saved: {filename}")


# 4. Bubble Chart (Seaborn)
def plot_metrics_relationship(df):
    """
    Visualize Likes vs Comments, with bubble size representing Shares.
    """
    # TODO: 12. Set figure size to 8 inches by 6 inches
    plt.figure(figsize=(8, 6))

    # TODO: 13. Create a Scatter Plot (Bubble Chart)
    # x="likes", y="comments"
    # size="shares" (This makes it a bubble chart)
    sns.scatterplot(
        data=df,
        x="likes",
        y="comments",
        size="shares",
        legend=True
    )

    # TODO: 14. Add title and labels
    # Title: "Likes vs Comments (Size = Shares)"
    plt.title("Likes vs Comments (Size = Shares)")
    plt.xlabel("Likes")
    plt.ylabel("Comments")

    filename = "metrics_relationship.png"

    # TODO: Save the plot
    plt.savefig(filename)

    print(f"Chart saved: {filename}")


# 5. Box Plot with Melt (Pandas + Seaborn)
def plot_engagement_distribution(df):
    """
    Compare distributions of Likes vs Comments vs Shares.
    """
    # TODO: 15. Reshape the data using df.melt()
    # Transforms the columns "likes", "comments", "shares" into rows
    # Hint: id_vars="post_id", value_vars=["likes", "comments", "shares"], var_name="metric", value_name="count"
    melted_df = df.melt(
        id_vars="post_id",
        value_vars=["likes", "comments", "shares"],
        var_name="metric",
        value_name="count"
    )

    # TODO: 16. Set figure size to 8 inches by 6 inches
    plt.figure(figsize=(8, 6))

    # TODO: 17. Create a Box Plot using the melted_df
    # x="metric", y="count", hue="metric"
    # palette="Set2", legend=False
    sns.boxplot(
        data=melted_df,
        x="metric",
        y="count",
        hue="metric",
        palette="Set2",
        legend=False
    )

    # TODO: 18. Add title and labels
    # Title: "Distribution of Engagement Metrics"
    plt.title("Distribution of Engagement Metrics")
    plt.xlabel("Metric")
    plt.ylabel("Count")

    filename = "engagement_distribution.png"

    # TODO: Save the plot
    plt.savefig(filename)

    print(f"Chart saved: {filename}")


if __name__ == "__main__":
    print("Social Media Engagement Analyzer Project\n")

    df = load_data()

    if df is not None:
        df = analyze_engagement(df)

        if "total_engagement" in df.columns:
            plot_engagement_composition(df)
            plot_metrics_relationship(df)
            plot_engagement_distribution(df)
        else:
            print("... Please complete the analyze_engagement function.")
    else:
        print("... Please complete the load_data function.")
