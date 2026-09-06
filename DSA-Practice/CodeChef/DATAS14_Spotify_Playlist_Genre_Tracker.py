"""
Problem: Spotify Playlist Genre Tracker Project (DATAS14)
Platform: CodeChef
Link: https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ03/problems/DATAS14
Date Solved: 2026-09-06
Difficulty: Medium
Topics: Pandas, Data Cleaning, Duplicate Removal, GroupBy Aggregation, Multi-Aggregation, Sorting

Approach:
    Load the playlist CSV into a DataFrame, then de-duplicate tracks on
    (Track, Artist) to avoid double-counting repeated entries. Compute genre
    popularity via value_counts(), analyze per-artist output within each
    genre via a two-key groupby, and produce a genre-level summary combining
    count + mean aggregations via .agg(). Finally sort the grouped artist
    counts descending to surface the most prolific artists.

Time Complexity:  O(n log n) — dominated by groupby's internal sort and the
                   final sort_values call over n rows.
Space Complexity: O(n) — for the cleaned DataFrame and the grouped/aggregated
                   result structures.
"""


# --------------------- Solution --------------------------------


import pandas as pd


# 1. Load Playlist Data
def load_playlist(filename):
    """
    Load CSV playlist data into a pandas DataFrame.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 2. Remove Duplicate Tracks
def remove_duplicates(df):
    """
    Remove duplicate songs based on Title + Artist combination.
    """

    # Keep only unique entries based on the 'Track' and 'Artist' columns
    cleaned_df = df.drop_duplicates(
        subset=["Track", "Artist"],
        keep="first"
    )
    return cleaned_df


# 3. Count Genre Popularity
def count_genre_frequency(df):
    """
    Count total songs in each genre.
    """

    # Calculate the frequency of each unique value in the 'Genre' column
    return df["Genre"].value_counts()


# 4. Analyze Artist Performance by Genre
def group_by_genre_and_artist(df):
    """
    Group by Genre + Artist and count tracks per artist.
    """
    # Create a grouping to count the number of tracks for every Artist within each Genre
    # Group by ("Genre", "Artist") and select the "Track" column

    grouped = df.groupby(["Genre", "Artist"])["Track"].count()
    return grouped


# 5. Multi-Aggregation Summary
def compute_genre_stats(df):
    """
    Calculate:
      - Total Songs per genre (count)
      - Average Popularity (mean, (0-100))
    """
    # Aggregate the data to find the 'count' of Tracks and 'mean' Popularity per Genre
    # Group by "Genre" and use .agg() with a dictionary
    # We need: 'Track': 'count' AND 'Popularity': 'mean'
    stats = df.groupby("Genre").agg({
        "Track": "count",
        "Popularity": "mean"
    })
    
    # Renaming columns for cleaner output
    # Also round average popularity to 2 decimal places (Code already written)
    if not stats.empty:
        # Rename columns for cleaner output
        stats.columns = ["Total_Songs", "Avg_Popularity"]
        return stats.round(2)
    return stats


# 6. Sort Results for Insights
def sort_top_artists(grouped_series):
    """
    Sort grouped Series (Genre + Artist track counts) in descending order.
    """
    # Sort values so the artists with the most songs appear first (descending)
    return grouped_series.sort_values(ascending=False)


if __name__ == "__main__":

    filename = 'spotify_playlist.csv'
    df = load_playlist(filename)

    if not df.empty:
        # Check initial count
        print(f"\nSongs Loaded: {len(df)}")

        # Remove duplicates
        df_clean = remove_duplicates(df)
        print(f"After Cleaning Duplicates: {len(df_clean)}")

        # Genre frequency
        genre_counts = count_genre_frequency(df_clean)
        print("\nSongs Per Genre:")
        print(genre_counts)

        # Artist performance per genre
        artist_grouped = group_by_genre_and_artist(df_clean)
        print("\nArtist Track Counts (Grouped):")
        # Show top 10 to save space
        print(artist_grouped.head(10)) 

        # Genre summary statistics
        genre_stats = compute_genre_stats(df_clean)
        print("\nGenre Performance Stats:")
        print(genre_stats)

        # Most active artists overall
        sorted_artists = sort_top_artists(artist_grouped)
        print("\nTop 5 Most Active Artists:")
        print(sorted_artists.head(5))
