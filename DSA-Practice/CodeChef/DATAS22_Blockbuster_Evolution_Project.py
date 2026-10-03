"""
Problem   : Blockbuster Evolution Project (DATAS22)
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ05/problems/DATAS22
Difficulty: Medium
Date      : 2026-10-03
Topics    : Pandas, Data Cleaning, GroupBy, Ranking, Expanding/Rolling Windows

Approach:
    1. Load movies.csv, returning an empty DataFrame if the file is missing.
    2. Parse 'released' to datetime and drop rows with missing 'gross'.
    3. Cast low-cardinality string columns to 'category' to cut memory use.
    4. Rank studios: groupby('company') -> sum gross -> rank(method='min',
       descending) so ties share a rank, then sort by rank.
    5. Industry growth: sort by release date, then expanding().sum() on gross.
    6. Trends: sort by release date, then rolling(3).mean() with NaN -> 0.

Complexity (n = number of movies, k = number of companies):
    Time : O(n log n), dominated by sorting by date (groupby and rank add
           O(n + k log k); load, clean, and rolling are O(n)).
    Space: O(n) for the DataFrame copies and the derived columns.
"""


# --------------------------------------- Solution ----------------------------------------------


import pandas as pd

# 1. Load Dataset
def load_dataset(filepath):
    """
    Load the CSV file and handle file not found errors.
    """
    try:
        # TODO: Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return pd.DataFrame()

# 2. Clean Data (Date Parsing & Removing Empty Rows)
def clean_data(df):
    """
    Parse the complex date format and remove rows with missing gross revenue.
    """
    # Step 1: Copying the dataframe to avoid modifying the original
    df_clean = df.copy()

    # TODO: Convert the 'released' column to datetime objects
    df_clean['released'] = pd.to_datetime(df_clean['released'])

    # TODO: Remove rows where 'gross' is NaN (Empty) to prevent calculation errors later
    df_clean = df_clean.dropna(subset=['gross'])

    # Step 4: Returning cleaned dataframe
    return df_clean

# 3. Optimize Memory
def optimize_memory(df):
    """
    Convert string columns with repeated values to 'category' type to save RAM.
    """
    # Copying the dataframe
    df_optimized = df.copy()

    # List of columns that are good candidates for categorical conversion
    categorical_cols = ['rating', 'genre', 'country', 'company']

    for col in categorical_cols:
        # Check if column exists before converting
        if col in df_optimized.columns:
            # TODO: Convert the column to 'category' type
            df_optimized[col] = df_optimized[col].astype('category')

    # Returning optimized dataframe
    return df_optimized

# 4. Studio Ranking (Grouped Ranking)
def rank_studios(df):
    """
    Rank production companies by their total gross revenue.
    """
    # TODO: Group by 'company' and sum the 'gross' revenue
    # Put observed=True in groupby to handle categorical data properly
    studio_gross = df.groupby('company', observed=True)['gross'].sum()

    # TODO: Rank the studios based on total gross (Highest gross = Rank 1)
    # Assign the same rank to studios with the same gross revenue
    ranks = studio_gross.rank(method='min', ascending=False)

    # TODO: Combine into a clean table
    # Columns: 'Total_Gross', 'Rank'
    ranking_table = pd.DataFrame({
        'Total_Gross': studio_gross,
        'Rank': ranks
    })

    # Sort the result by Rank in ascending order
    ranking_table = ranking_table.sort_values('Rank')

    return ranking_table

# 5. Industry Growth (Expanding Sums)
def calculate_industry_growth(df):
    """
    Calculate the cumulative gross revenue over time.
    """
    # TODO: Sort the dataframe by 'released' date (Essential for time-series calculations)
    df_sorted = df.sort_values('released').copy()

    # TODO: Calculate Expanding Sum for 'gross' to get cumulative industry gross
    df_sorted['cumulative_industry_gross'] = (
        df_sorted['gross'].expanding().sum()
    )

    # TODO: Return relevant columns
    return df_sorted[
        ['released', 'name', 'gross', 'cumulative_industry_gross']
    ]

# 6. Trend Analysis (Rolling Windows)
def analyze_recent_trends(df):
    """
    Calculate the '3-Movie Rolling Average' of Gross Revenue.
    """
    # Sort by date first to ensure the rolling window moves through time correctly
    df_sorted = df.sort_values('released').copy()

    # TODO: Calculate the Rolling Average
    # 1. Select 'gross' column
    # 2. Create a rolling window of 3
    # 3. Calculate the mean
    # 4. Fill NaN values with 0 (zero) for the first two entries
    df_sorted['rolling_avg_3_movies'] = (
        df_sorted['gross']
        .rolling(window=3)
        .mean()
        .fillna(0)
    )

    # TODO: Return relevant columns
    return df_sorted[
        ['released', 'name', 'gross', 'rolling_avg_3_movies']
    ]

if __name__ == "__main__":
    print("### Blockbuster Evolution Project ###")

    # 1. Load
    df_raw = load_dataset("movies.csv")

    if not df_raw.empty:
        # 2. Clean
        df_clean = clean_data(df_raw)

        # 3. Optimize
        df = optimize_memory(df_clean)

        # Check if we still have data after cleaning (e.g. dropping NaNs)
        if not df.empty:
            print(f"\n1. Data Loaded Successfully.")

            # 2. Rankings
            print("\n2. Top 5 Companies by Total Gross:")
            print(rank_studios(df).head())

            # 3. Cumulative Growth
            print("\n3. Industry Growth (First 5 Entries):")
            print(calculate_industry_growth(df).head())

            # 4. Rolling Trends
            print("\n4. Recent Trends (First 10 Entries):")
            print(analyze_recent_trends(df).head(10))
        else:
            print("Error: Dataframe is empty after cleaning.")
    else:
        print("Error: 'movies.csv' not found.")
