"""
Problem   : Weekly Fitness Progress Analyzer Project (DATAS07)
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ02/problems/DATAS07
Difficulty: Easy
Topics    : NumPy, Array Reshaping, Aggregate Functions, Vectorized Operations

Approach:
- Generate 7 days of random step counts with a fixed seed (np.random.randint).
- Reshape the 1D array into a (1,7) matrix to represent one week of data.
- Use np.sum/np.mean along axis=1 to get weekly total and daily average.
- Use np.argmax/np.argmin on the raw steps array to locate peak/lowest activity days.
- Use np.sort to get an ascending view of the week's step counts.

Time Complexity : O(n) — n = 7 (single pass for sum/mean/argmax/argmin), O(n log n) for sort
Space Complexity: O(n) — one array of size 7 plus its (1,7) reshape view
"""


# -------------------------- Solution ---------------------------------


import numpy as np


# 1. Generate Step Data
def generate_step_data():
    """
    Generate random step count data for 7 days.
    """
    # # Set seed for reproducibility (so we get the same random numbers every time) (DO NOT CHANGE THIS)
    np.random.seed(42)
    
    # TODO: Generate 7 random integers between 3000 and 12000
    steps = np.random.randint(3000, 12000, 7)
    
    return steps


# 2. Reshape Data
def reshape_weekly_data(steps):
    """
    Reshape the 1D step array into a 1x7 matrix (1 week, 7 days).
    """
    # TODO: Reshape 'steps' into a matrix with 1 row and 7 columns
    weekly_matrix = steps.reshape(1, 7)
    
    return weekly_matrix


# 3. Weekly Analysis
def analyze_weekly_data(weekly_matrix):
    """
    Calculate total weekly steps and daily average steps.
    """
    # TODO: Calculate sum along rows
    # Note: Since it's a matrix, the result will be an array like [total]. Access the first element [0].
    total_steps = np.sum(weekly_matrix, axis=1)[0]
    
    # TODO: Calculate mean along rows
    daily_average = np.mean(weekly_matrix, axis=1)[0]
    
    return total_steps, daily_average


# 4. Identify Peak Activity
def find_peak_activity(steps):
    """
    Identify the indices of the most and least active days.
    """
    # TODO: Find the index of the maximum value
    most_active_day_index = np.argmax(steps)
    
    # TODO: Find the index of the minimum value
    least_active_day_index = np.argmin(steps)
    
    return most_active_day_index, least_active_day_index


# 5. Sort Data
def sort_step_counts(steps):
    """
    Sort daily step counts in ascending order.
    """
    # TODO: Sort the steps array
    sorted_steps = np.sort(steps)
    
    return sorted_steps


if __name__ == "__main__":
    print("Weekly Fitness Progress Analyzer...\n")

    # Generate step data
    steps = generate_step_data()
    print(f"Daily Step Counts (Raw): {steps}")
    if steps is not None:
        # Reshape to weekly matrix
        weekly_matrix = reshape_weekly_data(steps)
        print(f"Weekly Matrix Shape: {weekly_matrix.shape}")

        # Analyze weekly data
        total, avg = analyze_weekly_data(weekly_matrix)
        print(f"\nTotal Weekly Steps: {total}")
        print(f"Average Daily Steps: {avg:.2f}")

        # Peaks 
        max_idx, min_idx = find_peak_activity(steps)
        print(f"\nMost Active Day Index: {max_idx} (Steps: {steps[max_idx]})")
        print(f"Least Active Day Index: {min_idx} (Steps: {steps[min_idx]})")

        # Sort steps
        sorted_steps = sort_step_counts(steps)
        print(f"\nSorted Steps: {sorted_steps}")
