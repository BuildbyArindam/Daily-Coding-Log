"""
Problem: Online Grocery Spending Insights Project (DATAS15)
Platform: CodeChef
Link: https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ03/problems/DATAS15
Difficulty: Medium
Topics: Pandas, Matplotlib, Data Visualization, GroupBy Aggregation, Pie Chart, Histogram
Date Solved: 2026-09-07

Approach:
    - Load grocery order data from CSV into a pandas DataFrame.
    - Group orders by 'Category' and sum 'Total_Price' to get category-wise
      spending totals.
    - Visualize category share of spending with a pie chart (% breakdown).
    - Visualize distribution of individual order values with a histogram
      to see whether orders skew cheap or expensive.

Time Complexity:  O(n) - single pass groupby/sum over n rows; histogram
                   binning and pie chart rendering are O(n) and O(k)
                   (k = number of categories) respectively.
Space Complexity: O(n) - DataFrame holds all n rows; category_totals is
                   O(k) additional space.
"""


# -------------------------- Solution --------------------------------


import pandas as pd

import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files

import matplotlib.pyplot as plt


# 1. Load Grocery Order Data
def load_grocery_data(filename):
    """
    Load CSV order data into a pandas DataFrame.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filename)
        print("Data loaded successfully.")

        # Return the DataFrame
        return df

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 2. Calculate Category Spending Totals
def calculate_category_spending(df):
    """
    Sum total spending for each item category.
    """
    # Group by 'Category' and sum the 'Total_Price' column
    category_totals = df.groupby("Category")["Total_Price"].sum()

    # Return the resulting Series
    return category_totals


# 3. Plot Pie Chart for Category Spending Share
def plot_category_pie(category_totals):
    """
    Create and save a pie chart of category spending distribution.
    Shows which category (e.g., Dairy, Fruits) consumes the most budget.
    """

    # Set figure size to 7 inches by 7 inches
    plt.figure(figsize=(7, 7))

    # Create a pie chart
    plt.pie(
        # Use the values from category_totals
        category_totals.values,

        # Use the index (category names) as labels
        labels=category_totals.index,

        # Show percentage up to 1 decimal place
        autopct="%.1f%%",

        # Slightly separate all slices using explode
        explode=[0.05] * len(category_totals)
    )

    # Set the plot title
    plt.title("Grocery Spending by Category")

    # Save the plot
    output_file = "category_spending_pie_chart.png"

    # Save the figure with tight layout
    plt.savefig(output_file, bbox_inches="tight")

    print(f"Pie chart saved to {output_file}")


# 4. Plot Histogram of Order Value
def plot_order_histogram(df):
    """
    Create and save a histogram of individual order values.
    Shows the distribution of order costs (Are most orders cheap or expensive?).
    """

    # Set figure size to 8 inches by 5 inches
    plt.figure(figsize=(8, 5))

    # Create a histogram for the 'Total_Price' column
    plt.hist(
        df["Total_Price"],

        # Set the number of bins to 10
        bins=10,

        # Set the Bar color
        color="skyblue",

        # Set the Border color
        edgecolor="black",

        # Set the Transparency value
        alpha=0.7
    )

    # Add Title and Labels
    plt.title("How Much Do Customers Spend? (Order Value Distribution)")
    plt.xlabel("Total Bill Amount ($)")
    plt.ylabel("Number of Orders")

    # Add gridlines only to the y-axis with transparency of 0.5
    plt.grid(axis="y", alpha=0.5)

    # Save the plot
    output_file = "order_value_histogram.png"

    # Save the figure
    plt.savefig(output_file)

    print(f"Histogram saved to {output_file}")


if __name__ == "__main__":

    # Load data
    filename = "grocery_orders.csv"
    df = load_grocery_data(filename)

    if not df.empty:
        print(f"Total Transactions: {len(df)}")

        # 1. Analysis: Category Spending
        category_totals = calculate_category_spending(df)
        print("\nSpending Breakdown by Category:")
        print(category_totals)

        # 2. Visualization: Pie Chart
        print("\nGenerating Pie Chart...")
        plot_category_pie(category_totals)

        # 3. Visualization: Histogram
        print("\nGenerating Histogram...")
        plot_order_histogram(df)
