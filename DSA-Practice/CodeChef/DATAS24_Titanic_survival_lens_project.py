"""
Problem   : Titanic Survival Lens Project
Platform  : CodeChef (Data Analysis & Visualization Projects, DATASPRJ05)
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ05/problems/DATAS24
Difficulty: Medium
Topics    : Pandas, Seaborn, Data Visualization, EDA, Feature Engineering
Date      : 2026-10-03

Approach:
  1. Load the Titanic CSV and validate that the required columns exist.
  2. Clean the data: drop rows with a missing Embarked value, impute Age and
     Fare with the median, and engineer FamilySize = SibSp + Parch + 1.
  3. FacetGrid: survival-rate bar plots by Embarked, split by Sex (rows) and
     Pclass (columns), with a 0.5 reference line.
  4. JointGrid: Age vs log1p(Fare) scatter coloured by Survived, with KDE
     marginals (log transform reduces Fare skew).
  5. PairGrid: pairwise scatter of Age, Fare and FamilySize, hued by Survived.
  Plots are saved as PNGs using the headless "Agg" backend.

Complexity (n = rows, k = number of plotted features = 3):
  Time : O(n) for cleaning and feature engineering; O(n) for the FacetGrid,
         JointGrid and KDE plots (KDE adds a constant grid-evaluation factor);
         O(n * k^2) for the PairGrid.
  Space: O(n) for the DataFrame copies (df_clean, plot_df).
"""


# ------------------------------------------- Solution ----------------------------------------------------


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
# Force Matplotlib to work without GUI
matplotlib.use("Agg")
# Set seaborn theme
sns.set_theme(style="whitegrid", palette="muted")

# 1. Load Titanic Dataset
def load_titanic_data(filepath):
    """
    Load Titanic dataset from CSV file.
    """
    try:
        # Read the CSV file into a dataframe
        df = pd.read_csv(filepath)
        print("Titanic dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

# 2. Clean Data & Feature Engineering
def preprocess_titanic_data(df):
    """
    Clean missing values and create new features
    for analysis and visualization.
    """
    # Copying dataframe to avoid modifying original
    df_clean = df.copy()
    # Required columns
    required_cols = [
        "Survived", "Sex", "Pclass", "Embarked",
        "Age", "Fare", "SibSp", "Parch"
    ]
    missing = [col for col in required_cols if col not in df_clean.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    # Remove rows with missing embarkation
    df_clean = df_clean.dropna(subset=["Embarked"])
    # Fill missing Age using the median value of Age column
    df_clean["Age"] = df_clean["Age"].fillna(df_clean["Age"].median())
    # Fill missing Fare using the median value of Fare column
    df_clean["Fare"] = df_clean["Fare"].fillna(df_clean["Fare"].median())
    # Feature Engineering: Family Size
    # Calculate FamilySize = SibSp + Parch + 1
    df_clean["FamilySize"] = df_clean["SibSp"] + df_clean["Parch"] + 1
    print("Data cleaned and features engineered successfully.")
    return df_clean

# 3. FacetGrid — Survival Rate Analysis
def plot_demographic_facet(df):
    # FacetGrid for survival rate by Sex, Pclass and Embarked
    # Initialize FacetGrid
    # - data: The dataframe
    # - Split the grid rows based on Gender
    # - Split the grid columns based on Passenger Class
    # - Enable margin titles
    g = sns.FacetGrid(
        data=df,
        row="Sex",
        col="Pclass",
        margin_titles=True
    )
    # Bar plot of survival rate by Embarked within each facet
    # Map a plotting function to the grid
    # - Plotting Function: sns.barplot
    # - Map "Port of Embarkation" to the X-axis
    # - Map "Survival Status" to the Y-axis
    # - Set color to "skyblue"
    # - Set edgecolor to "black"
    # - Disable error bars
    g.map_dataframe(
        sns.barplot,
        x="Embarked",
        y="Survived",
        color="skyblue",
        edgecolor="black",
        errorbar=None
    )
    # Add a reference line at 0.5 survival rate
    # Color the line red and use dashed style
    g.refline(
        y=0.5,
        color="red",
        linestyle="--"
    )
    # X and Y labels
    g.set_axis_labels("Port of Embarkation", "Survival Rate (0-1)")
    # Adjust titles and layout
    g.figure.subplots_adjust(top=0.90)
    # Overall title of the FacetGrid
    g.figure.suptitle("Survival Rate by Gender, Class & Embarkation")
    # Saving the plot
    plt.savefig("titanic_facet_bar.png")
    print("FacetGrid plot saved.")

# 4. JointGrid — Age vs Fare
def plot_fare_age_joint(df):
    # Transform Fare for better visualization
    plot_df = df.copy()
    # Log-transform the 'Fare' column using np.log1p() to reduce skewness
    plot_df["Log_Fare"] = np.log1p(plot_df["Fare"])
    # JointGrid for Age vs Log(Fare)
    # Initialize JointGrid
    # - data: The transformed dataframe
    # - Map "Age" to the X-axis
    # - Map the new "Log_Fare" to the Y-axis
    g = sns.JointGrid(
        data=plot_df,
        x="Age",
        y="Log_Fare"
    )
    # Scatter plot with survival hue
    # Plot the joint chart (center) using sns.scatterplot
    # - Color the points based on "Survival Status" (hue)
    # - data: The transformed dataframe
    # - Use the palette: {0: "red", 1: "green"}
    # - Transparency (alpha): 0.6
    # - Point size (s): 50
    g.plot_joint(
        sns.scatterplot,
        data=plot_df,
        hue="Survived",
        palette={0: "red", 1: "green"},
        alpha=0.6,
        s=50
    )
    # Marginal KDE plots for Age and Log(Fare)
    # Plot the marginal charts (sides) using sns.kdeplot
    # - Enable fill under the curve
    # - Set transparency (alpha) to 0.3
    # - Set color to "gray"
    g.plot_marginals(
        sns.kdeplot,
        fill=True,
        alpha=0.3,
        color="gray"
    )
    # X and Y labels
    g.set_axis_labels("Age", "Fare (Log Scale)")
    # Adjust titles and layout
    g.figure.subplots_adjust(top=0.90)
    # Overall title of the JointGrid
    g.figure.suptitle("Survival Clusters: Age vs Log(Fare)")
    # Saving the plot
    plt.savefig("titanic_joint_kde.png")
    print("JointGrid plot saved.")

# 5. PairGrid — Numeric Relationships
def plot_pair_matrix(df):
    # PairGrid for selected numeric features
    features = ["Age", "Fare", "FamilySize"]
    # Create PairGrid with survival hue
    # Initialize PairGrid
    # - data: The dataframe
    # - Limit variables to the 'features' list defined above
    # - Color the charts based on "Survival Status"
    # - Use palette: {0: "red", 1: "green"}
    g = sns.PairGrid(
        data=df,
        vars=features,
        hue="Survived",
        palette={0: "red", 1: "green"}
    )
    # Scatter plots in the grid
    # Map sns.scatterplot to the grid
    # - Set transparency (alpha) to 0.6
    # - Set point size (s) to 30
    g.map(
        sns.scatterplot,
        alpha=0.6,
        s=30
    )
    # Legend
    g.add_legend(title="Survived")
    # Adjust titles and layout
    g.figure.subplots_adjust(top=0.90)
    # Overall title of the PairGrid
    g.figure.suptitle("Passenger Feature Relationships")
    # Saving the plot
    plt.savefig("titanic_pair_grid.png")
    print("PairGrid plot saved.")

if __name__ == "__main__":
    df_raw = load_titanic_data("titanic_dataset.csv")
    if not df_raw.empty:
        df = preprocess_titanic_data(df_raw)
        print("\nGenerating FacetGrid...")
        plot_demographic_facet(df)
        print("\nGenerating JointGrid...")
        plot_fare_age_joint(df)
        print("\nGenerating PairGrid...")
        plot_pair_matrix(df)
