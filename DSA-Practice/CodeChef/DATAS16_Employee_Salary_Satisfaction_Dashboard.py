"""
Problem   : Employee Salary & Satisfaction Dashboard Project (DATAS16)
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ03/problems/DATAS16
Difficulty: Medium
Topics    : Pandas, Seaborn, Matplotlib, Data Visualization, EDA, Countplot, Boxplot, Violinplot, GroupBy-style Comparison
Date      : 2026-09-07

Approach:
    Load employee records into a pandas DataFrame, then build three
    diagnostic visualizations with seaborn/matplotlib:
      1. Countplot  - department headcount split by gender
      2. Boxplot    - salary spread per department
      3. Violinplot - satisfaction score density per department,
                       split by gender (male vs female halves)
    Each chart is saved as a PNG via a headless Agg backend so the
    script runs without a display (CI/server-friendly).

Time complexity : O(n) — one pass over the n employee rows per plot
                   (pandas/seaborn aggregation is linear in dataset size).
Space complexity : O(n) — the DataFrame and derived groupings held in memory.
"""


# ----------------------- Solution ----------------------------


import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")   # Headless mode for saving files
import matplotlib.pyplot as plt


# 1. Load Employee Data
def load_employee_data(filename):
    """
    Load CSV dataset into a pandas DataFrame.
    """
    try:
        # Read the CSV file into a dataframe
        df = pd.read_csv(filename)

        print("Data loaded successfully.")

        # Return the dataframe
        return df

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 2. Plot Department Headcounts
def plot_department_counts(df):
    """
    Create a countplot showing how many employees work in each department.
    """
    # Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10, 6))

    # Create a countplot
    # - Department on X-axis
    # - Gender as hue
    # - data: df
    # - palette: viridis
    sns.countplot(
        x="Department",
        hue="Gender",
        data=df,
        palette="viridis"
    )

    # Set the title
    plt.title("Employee Count by Department")

    # Set axis labels
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")

    # Set the legend title
    plt.legend(title="Gender")

    # Rotate x-axis labels by 45 degrees
    plt.xticks(rotation=45)

    output = "department_headcount.png"

    # Save the figure
    plt.savefig(output, bbox_inches="tight")

    print(f"Saved: {output}")


# 3. Plot Salary Distribution
def plot_salary_box(df):
    """
    Compare salary ranges across departments using boxplots.
    """
    # Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10, 6))

    # Create a boxplot
    # - Department on X-axis
    # - Salary on Y-axis
    # - data: df
    # - Disable the legend
    sns.boxplot(
        x="Department",
        y="Salary",
        data=df,
        legend=False
    )

    # Set the title
    plt.title("Salary Distribution by Department")

    # Set axis labels
    plt.xlabel("Department")
    plt.ylabel("Annual Salary ($)")

    # Rotate x-axis labels by 45 degrees
    plt.xticks(rotation=45)

    output = "salary_boxplot.png"

    # Save the figure
    plt.savefig(output, bbox_inches="tight")

    print(f"Saved: {output}")


# 4. Plot Employee Satisfaction
def plot_satisfaction_violin(df):
    """
    Show satisfaction score distribution using violin plots.
    """

    # Set the figure size to 10 inches by 6 inches
    plt.figure(figsize=(10, 6))

    # Create a violinplot
    # - Department on X-axis
    # - Satisfaction on Y-axis
    # - Gender as hue
    # - split=True merges Male/Female halves
    # - inner="quartile" shows quartile lines
    # - palette="muted"
    sns.violinplot(
        x="Department",
        y="Satisfaction",
        hue="Gender",
        data=df,
        split=True,
        inner="quartile",
        palette="muted"
    )

    # Set the title
    plt.title("Employee Satisfaction Density (Male vs Female)")

    # Set axis labels
    plt.xlabel("Department")
    plt.ylabel("Satisfaction Score (0-10)")

    # Set the legend title
    plt.legend(title="Gender")

    # Rotate x-axis labels by 45 degrees
    plt.xticks(rotation=45)

    output = "satisfaction_violin.png"

    # Save the figure
    plt.savefig(output, bbox_inches="tight")

    print(f"Saved: {output}")


if __name__ == "__main__":
    file = "employees.csv"
    df = load_employee_data(file)

    if not df.empty:
        print(f"Total Employees: {len(df)}")

        # Who works here?
        print("\nGenerating Department Count Chart...")
        plot_department_counts(df)

        # How much do they make?
        print("\nGenerating Salary Box Plot...")
        plot_salary_box(df)

        # Are they happy?
        print("\nGenerating Satisfaction Violin Plot...")
        plot_satisfaction_violin(df)
