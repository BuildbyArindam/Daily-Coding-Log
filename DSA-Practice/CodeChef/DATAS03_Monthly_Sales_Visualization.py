"""
Problem: Monthly Sales Visualization Project (DATAS03)
Platform: CodeChef
Link: https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ01/problems/DATAS03
Date: 2026-08-31
Difficulty: Medium
Topics: Matplotlib, Data Visualization, Line/Bar Charts

Approach:
Hardcode monthly sales data as parallel lists, then render two
separate Matplotlib figures (line chart for trend, bar chart for
comparison) using the non-interactive "Agg" backend so it runs
headless. Each chart is built with its own figure/axes config
(title, labels, grid, legend) and saved to disk as a PNG.

Time Complexity:  O(n) — n = number of months (fixed at 12), one pass
                   per chart to plot the data points.
Space Complexity: O(n) — stores month labels and sales values in memory;
                   no extra data structures beyond the two lists.
"""


# ----------------------------- Solution ---------------------------------


import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt


# 1. Load Data
def load_sales_data():
    """
    Returns lists of months and sales figures.
    """
    # Create a list of strings for months
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    # Create a list of integers for sales amounts
    sales = [
        12000, 15000, 17000, 16000, 18000, 20000,
        22000, 21000, 19000, 23000, 25000, 27000
    ]

    return months, sales


# 2. Line Plot (Trend)
def plot_sales_trend(months, sales):
    """
    Create a line chart and save it to a file.
    """
    # Set the figure size to (10, 6)
    plt.figure(figsize=(10, 6))

    # Plot the data
    plt.plot(
        months,
        sales,
        color="blue",
        marker="o",
        linestyle="-",
        linewidth=2,
        label="Monthly Sales"
    )

    # Add title and axis labels
    plt.title("Monthly Sales Trend (2025)")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount ($)")

    # Enable grid and show legend
    plt.grid(True)
    plt.legend()

    # Save the plot
    filename = "sales_trend.png"
    plt.savefig(filename)

    print("Saving Line Chart as 'sales_trend.png'...")
    print(f"Chart saved: {filename}")


# 3. Bar Chart (Comparison)
def plot_sales_bar_chart(months, sales):
    """
    Create a bar chart and save it to a file.
    """
    # Set the figure size to (10, 6)
    plt.figure(figsize=(10, 6))

    # Plot the data as a bar chart
    plt.bar(
        months,
        sales,
        color="orange",
        label="Monthly Sales"
    )

    # Add title and axis labels
    plt.title("Monthly Sales Comparison")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount ($)")

    # Enable grid and show legend
    plt.grid(True)
    plt.legend()

    # Save the plot
    filename = "sales_bar_chart.png"
    plt.savefig(filename)

    print("Saving Bar Chart as 'sales_bar_chart.png'...")
    print(f"Chart saved: {filename}")


if __name__ == "__main__":
    print("Monthly Sales Visualization Project\n")

    # Loading data
    months, sales = load_sales_data()

    # Plotting
    plot_sales_trend(months, sales)
    plot_sales_bar_chart(months, sales)
