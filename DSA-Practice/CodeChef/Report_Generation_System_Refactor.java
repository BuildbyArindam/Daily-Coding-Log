"""
Problem: Report Generation System Refactor
Platform: CodeChef
Link: https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ04/problems/DATAS18
Date Solved: 2026-09-13
Difficulty: Medium
Topics: Pandas, Data Cleaning, GroupBy Aggregation, DateTime Parsing, Sorting/Ranking

Approach:
Load flight CSV and parse FlightDate to datetime. Fill missing DepartureDelay
values with 0 (treated as on-time). Extract day-of-week as a feature via
dt.day_name(). Aggregate DepartureDelay per Airline (mean, count) to rank
airlines by reliability, and aggregate per Day_Name to find the worst
average-delay day of the week.

Time Complexity: O(n log n) — dominated by groupby + sort_values on n rows
Space Complexity: O(n) — one DataFrame copy plus grouped aggregates
"""


// ------------------------------ Solution ---------------------------------------


import pandas as pd

FILE_NAME = "flights.csv"

# 1. Data Loading and Data Parsing
def load_flight_data(filename):
    """
    Load flight dataset and parse dates from 'FlightDate'.
    """
    try:
        # TODO: Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(filename)

        # Validation: Check if required column exists
        if "FlightDate" not in df.columns:
            print("Error: 'FlightDate' column is missing in the CSV.")
            return pd.DataFrame()

        # TODO: Parse the "FlightDate" column into datetime format
        # Make sure to specify the correct date format (YYYY-MM-DD)
        df["FlightDate"] = pd.to_datetime(
            df["FlightDate"],
            format="%Y-%m-%d"
        )
        
        return df
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()


# 2. Data Cleaning
def clean_delay_data(df):
    """
    Assumption: If delay is NaN (empty), it means the flight was On Time (0 delay).
    """

    # TODO: Fill missing values (NaN) in the 'DepartureDelay' column with 0
    if "DepartureDelay" in df.columns:
        df["DepartureDelay"] = df["DepartureDelay"].fillna(0)
    
    return df


# 3. Feature Extraction
def extract_day_features(df):
    """
    Extract the 'Day Name' (Monday, Tuesday...) from the Date column.
    """

    # TODO: Get the name of the day (e.g., "Monday") from the "FlightDate" column
    # Hint: Use Pandas date accessors to find the day name
    df["Day_Name"] = df["FlightDate"].dt.day_name()
    
    return df


# 4. Statistical Analysis
def airline_reliability_stats(df):
    """
    Calculate the Average Departure Delay and Total Flights for each airline.
    """
    # TODO: Group data by "Airline" and calculate two statistics for "DepartureDelay":
    # 1. The Average (mean) delay
    # 2. The Total count of flights
    stats = df.groupby("Airline")["DepartureDelay"].agg(["mean", "count"])
    

    # Renaming columns for clarity
    if not stats.empty:
        stats = stats.rename(columns={"mean": "Avg_Delay", "count": "Total_Flights"})
        
        # Round the average delay to 2 decimal places
        stats["Avg_Delay"] = stats["Avg_Delay"].round(2)
    
    return stats


# 5. Ranking & Sorting
def rank_airlines(stats_df):
    """
    Rank airlines from Most Reliable (Lowest Delay) to Least Reliable.
    """
    # TODO: Sort the airlines so that the one with the LOWEST "Avg_Delay" comes first
    sorted_stats = stats_df.sort_values(by="Avg_Delay", ascending=True)
    
    return sorted_stats


# 6. Pattern Identification
def identify_delayed_days(df):
    """
    Find which day of the week has the worst delays on average.
    """
    # TODO: Find the average "DepartureDelay" for each "Day_Name"
    day_stats = df.groupby("Day_Name")["DepartureDelay"].mean()
    
    # TODO: Sort the results so the day with the HIGHEST delay comes first
    # Round the result to 2 decimal places
    sorted_days = day_stats.sort_values(ascending=False).round(2)
    
    return sorted_days


if __name__ == "__main__":
    print("### FlightFlow Analysis ###")

    # 1. Load Data
    raw_df = load_flight_data(FILE_NAME)

    if not raw_df.empty:
        # 2. Clean Data
        clean_df = clean_delay_data(raw_df)
        print(f"Data Loaded & Cleaned: {clean_df.shape[0]} flights processed.")

        # 3. Feature Extraction
        enhanced_df = extract_day_features(clean_df)
        
        # 4. Reliability Analysis
        stats = airline_reliability_stats(enhanced_df)
        ranked = rank_airlines(stats)
        
        print("\nMost Reliable Airlines (Lowest Avg Delay):")
        print(ranked.head(3))
        
        print("\nLeast Reliable Airlines (Highest Avg Delay):")
        print(ranked.tail(3))

        # 5. Pattern Analysis
        worst_days = identify_delayed_days(enhanced_df)

        print("\nWorst Days to Fly (Highest Avg Delay):")
        print(worst_days.head(3))
    
    else:
        print("Analysis could not proceed due to data loading errors.")
