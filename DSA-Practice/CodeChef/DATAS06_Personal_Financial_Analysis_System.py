"""
Platform     : CodeChef
Problem      : Personal Financial Analysis System Project (DATAS06)
Link         : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ01/problems/DATAS06
Date Solved  : 2026-09-01
Difficulty   : Medium
Topics       : Pandas, NumPy, Data Cleaning, GroupBy Aggregation, Descriptive Statistics

Approach:
    Built a small personal-finance pipeline using pandas + NumPy:
    1. load_data()      -> construct a DataFrame from raw income/expense records
    2. clean_data()     -> parse dates with errors='coerce', drop unparseable
                            rows (NaT), and filter out invalid amounts
                            (<= 0 or NaN) in one boolean mask
    3. calculate_savings()          -> groupby('type').sum() to get
                            Income vs Expense totals, then Income - Expense
    4. analyze_expenses_by_category() -> groupby('category').sum(),
                            sorted descending, for spend-by-category breakdown
    5. calculate_advanced_stats()   -> NumPy mean/median/max/min/std on the
                            expense array for quick financial insights

Time Complexity : O(n log n)  -- dominated by sort_values() in the
                   category breakdown; all groupby/filter/date-parse
                   steps are O(n)
Space Complexity : O(n) -- a constant number of derived DataFrames,
                   each bounded by the size of the cleaned input
"""


# -------------------------- Solution ----------------------------------


import pandas as pd
import numpy as np

# 1. Load Financial Data
def load_data():
    """
    Create and return a DataFrame containing personal income and expense data.
    """
    # Pre-filled data (DO NOT EDIT THIS)
    data = {
        "date": [
            "2025-01-01", "2025-01-03", "2025-01-05", "2025-01-08",
            "2025-01-10", "2025-01-12", "2025-01-15", "2025-01-18",
            "2025-01-20", "2025-01-25", "2025-01-28", "2025-01-30",
            "2025-02-05", "Invalid Date", "2025-02-28"
        ],
        "type": [
            "Income", "Expense", "Expense", "Income",
            "Expense", "Expense", "Expense", "Expense",
            "Expense", "Income", "Expense", "Expense",
            "Expense", "Expense", "Income"
        ],
        "category": [
            "Salary", "Food", "Transport", "Freelance",
            "Rent", "Dining Out", "Shopping", "Entertainment",
            "Utilities", "Salary", "Groceries", "Shopping",
            "Transport", "Food", "Bonus"
        ],
        "amount": [
            50000, 1200, 800, 15000,
            18000, 2500, -5000, 2000,
            3000, 50000, 4500, 7000,
            np.nan, 1500, 6000
        ]
    }

    # TODO: 1. Create a Pandas DataFrame from the dictionary
    df = pd.DataFrame(data)

    return df


# 2. Data Cleaning
def clean_data(df):
    """
    Clean and prepare the dataset:
    - Convert date to datetime objects
    - Remove invalid amounts (<= 0 or NaN)
    """
    # TODO: 2. Convert 'date' column to datetime
    # Critical: Use errors='coerce' to handle "Invalid Date" strings
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # TODO: 3. Drop rows where date parsing failed (NaT values)
    df = df.dropna(subset=["date"])

    # TODO: 4. Filter the DataFrame to keep only positive amounts (> 0)
    # This automatically removes negative typos (-5000) and NaNs
    df = df[df["amount"] > 0]

    # TODO: 5. Return cleaned DataFrame
    return df


# 3. Monthly Summary (Income vs Expense)
def calculate_savings(df):
    """
    Calculate total income, total expense, and remaining savings.
    """
    # TODO: 6. Find Summary by grouping 'type' and summing 'amount'
    summary = df.groupby("type")["amount"].sum()

    total_income = 0
    total_expense = 0

    # TODO: 7. Extract Income and Expense safely (default to 0 if missing)
    if summary is not None:
        total_income = summary.get("Income", 0)
        total_expense = summary.get("Expense", 0)

    # TODO: 8. Calculate Savings (Income - Expense)
    savings = total_income - total_expense

    # TODO: 9. Create a results DataFrame
    result = pd.DataFrame({
        "Total Income": [total_income],
        "Total Expense": [total_expense],
        "Net Savings": [savings]
    })

    # Return the summary DataFrame
    return result


# 4. Category-wise Analysis
def analyze_expenses_by_category(df):
    """
    Analyze expenses by category, sorted by highest spending.
    """
    # TODO: 10. Filter the DataFrame to include ONLY "Expense" types
    expense_df = df[df["type"] == "Expense"]

    # TODO: 11. Create the category summary
    # Steps:
    # 1. Group by 'category'
    # 2. Sum the 'amount'
    # 3. Sort values descending (highest expense first)
    # 4. Reset index for a clean DataFrame
    category_summary = (
        expense_df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return category_summary


# 5. Financial Insights (NumPy Integration)
def calculate_advanced_stats(df):
    """
    Use NumPy to calculate advanced statistical insights on expenses.
    """
    # TODO: 12. Filter for "Expense" rows and convert 'amount' column to a NumPy array
    expense_values = df[df["type"] == "Expense"]["amount"].to_numpy()

    if len(expense_values) > 0:
        # TODO: 13. Calculate stats using NumPy functions
        insights = {
            "Average Expense": np.mean(expense_values),
            "Median Expense": np.median(expense_values),
            "Max Expense": np.max(expense_values),
            "Min Expense": np.min(expense_values),
            "Std Dev": np.std(expense_values)
        }
    else:
        insights = {}

    # TODO: 14. Convert the insights dictionary to a DataFrame for better display
    insights_df = pd.DataFrame([insights])

    return insights_df


if __name__ == "__main__":
    print("Personal Financial Analysis System\n")

    # 1. Load Data
    df = load_data()
    print("Financial data loaded successfully!")

    # 2. Data Cleaning
    df = clean_data(df)
    if df is not None:
        print("\nData cleaned successfully!")
        print(df.head())

    # 3. Monthly Summary (Income vs Expense)
    print("\nMonthly Savings Summary:")
    print(calculate_savings(df))

    # 4. Category-wise Analysis
    print("\nExpense Breakdown by Category:")
    print(analyze_expenses_by_category(df))

    # 5. Financial Insights
    print("\nNumPy Statistics:")
    print(calculate_advanced_stats(df))
