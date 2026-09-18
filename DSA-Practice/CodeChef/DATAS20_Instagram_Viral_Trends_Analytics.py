"""
Problem   : Instagram Viral Trends Analytics Project
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ04/problems/DATAS20
Date      : 2026-09-18
Difficulty: Medium
Topics    : EDA, correlation analysis, linear regression, residual analysis,
            outlier detection, data visualization (seaborn/matplotlib)

Approach:
    1. Load Instagram post dataset from CSV.
    2. Compute and visualize correlation between engagement metrics
       (likes, comments, shares, saves, reach) via a heatmap.
    3. Fit a regression line to study hashtag count vs. reach trend.
    4. Use residual analysis (observed - expected reach) to flag
       viral outlier posts that over/under-perform relative to the
       hashtag-count trend.

Complexity:
    Time  : O(n) for loading + O(k^2) for the k x k correlation matrix
            (k = number of engagement columns, k << n), plus O(n log n)
            for the regression fit — overall ~O(n) for n posts.
    Space : O(n) to hold the dataframe, O(k^2) for the correlation matrix.
"""


# ------------------------------ Solution --------------------------------------------


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib
matplotlib.use("Agg")  
FILE_NAME = "instagram_dataset.csv"
sns.set_theme(style="whitegrid")

def load_instagram_data(filename):
    """
    Loading Instagram post dataset.
    """
    try:
        df = pd.read_csv(filename)
        print(f"Data Loaded Successfully: {len(df)} posts.")
        print(f"Columns: {list(df.columns)}")
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()

def plot_engagement_correlation(df):
    """
    Visualize correlation between engagement metrics using a Heatmap.
    """
    engagement_cols = [
        "likes",
        "comments",
        "shares",
        "saves",
        "reach"
    ]
    corr_matrix = df[engagement_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )
    plt.title("Instagram Engagement Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("engagement_correlation_heatmap.png")
    print("Saved: engagement_correlation_heatmap.png")

def plot_hashtag_vs_reach(df):
    """
    Analyze relationship between hashtags and reach using Regression.
    """
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x="hashtags_count",
        y="reach",
        data=df,
        scatter_kws={"color": "green"},
        line_kws={"color": "red"}
    )
    plt.title("Hashtag Count vs. Reach Trend")
    plt.xlabel("Number of Hashtags")
    plt.ylabel("Post Reach")
    plt.tight_layout()
    plt.savefig("hashtag_reach_trend.png")
    print("Saved: hashtag_reach_trend.png")

def plot_residual_analysis(df):
    """
    Use a Residual Plot to see 'outlier' performance.
    Points far from 0 line = Posts performing much better/worse than expected.
    """
    plt.figure(figsize=(10, 6))
    sns.residplot(
        x="hashtags_count",
        y="reach",
        data=df,
        color="purple"
    )
    plt.axhline(y=0, color="black", linestyle="--")
    plt.title("Residual Analysis: Viral Outliers (Observed - Expected)")
    plt.xlabel("Number of Hashtags")
    plt.ylabel("Residual Reach (Deviation)")
    plt.tight_layout()
    plt.savefig("viral_residual_analysis.png")
    print("Saved: viral_residual_analysis.png")

if __name__ == "__main__":
    print("### Instagram Viral Trends Analytics ###")
    df = load_instagram_data(FILE_NAME)
    if not df.empty:
        plot_engagement_correlation(df)
        plot_hashtag_vs_reach(df)
        plot_residual_analysis(df)
    else:
        print("Analysis stopped.")
