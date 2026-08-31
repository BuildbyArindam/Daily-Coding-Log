"""
Problem   : Netflix Library Explorer Project
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ01/problems/DATAS02
Date      : 2026-08-31
Difficulty: Cakewalk / Easy (Data Analysis track)
Topics    : Pandas, Data Loading, Exploratory Data Analysis, Filtering, Sorting, Value Counts

Approach:
    Load the Netflix dataset into a Pandas DataFrame and perform a
    sequence of EDA operations: inspect shape/columns, count content
    type distribution (Movie vs TV Show), filter titles released after
    2015, find the top 5 most common ratings, and sort content by
    release year (descending). Each step is isolated into its own
    function for readability and reuse.

Complexity:
    Time  : O(n log n) overall — dominated by sort_values() in
            sort_by_release_year(); value_counts() and boolean
            filtering are O(n).
    Space : O(n) — filtering and sorting create new DataFrames
            proportional to dataset size.
"""


# --------------------------------- Solution -----------------------------------


import pandas as pd


# 1. Load Netflix dataset
def load_data():
    """
    TODO:
    Load the Netflix dataset from the CSV file:
    - File path: "./netflix.csv"

    Print:
    - First 5 rows showing: title, type, release_year

    Return:
        Pandas DataFrame
    """

    df = pd.read_csv("./netflix.csv")
    print("Dataset loaded successfully!")

    print("\nSample Data (first 5 rows):")
    print(df[["title", "type", "release_year"]].head())

    return df


# 2. Display basic dataset information
def explore_dataset(df):
    """
    TODO:
    Print:
    - Shape of the dataset
    - Column names of the dataset
    """

    print("\nDataset Overview:")
    print("Shape of the dataset:", df.shape)
    print("Column Names:", df.columns.tolist())


# 3. Count Movies vs TV Shows
def count_content_types(df):
    """
    TODO:
    Count and print how many Movies and TV Shows are present.
    """

    print("\nContent Type Distribution:")
    content_counts = df["type"].value_counts()
    print(content_counts)


# 4. Filter content released after 2015
def filter_recent_content(df):
    """
    TODO:
    - Filter content released after 2015
    - Print first 5 rows showing: title, type, release_year

    Return:
        Filtered DataFrame
    """

    recent_content = df[df["release_year"] > 2015]
    print("\nContent Released After 2015:")
    print(recent_content[["title", "type", "release_year"]].head())

    return recent_content


# 5. Top 5 most common ratings
def top_ratings(df):
    """
    TODO:
    Print the top 5 most common content ratings.
    """

    print("\nTop 5 Content Ratings:")
    ratings = df["rating"].value_counts().head(5)
    print(ratings)


# 6. Sort content by release year (latest first)
def sort_by_release_year(df):
    """
    TODO:
    Sort the content by release year in descending order
    and print first 5 rows showing: title, type, release_year
    """

    sorted_df = df.sort_values(by="release_year", ascending=False)

    print("\nLatest Content on Netflix:")
    print(sorted_df[["title", "type", "release_year"]].head())


if __name__ == "__main__":
    print("Netflix Library Explorer Project\n")

    df = load_data()
    explore_dataset(df)
    count_content_types(df)
    recent_df = filter_recent_content(df)
    top_ratings(df)
    sort_by_release_year(df)
