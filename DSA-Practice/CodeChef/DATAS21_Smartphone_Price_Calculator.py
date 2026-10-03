"""
Problem   : Smartphone Price Calculator Project
Platform  : CodeChef (Data Analysis & Visualization Projects, DATASPRJ05)
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ05/problems/DATAS21
Difficulty: Medium
Topics    : NumPy, Pandas, Linear Algebra, Linear Regression, Data Preprocessing
Date      : 2026-10-03

Approach:
    1. Load smartphones.csv with Pandas and pull out 5 feature columns
       (RAM, storage, battery, rear camera, rating) plus the price target.
    2. Scale battery capacity (/100) so all features have similar magnitude.
    3. Price band = 5th to 95th percentile (np.percentile) to ignore outliers.
    4. Weighted tech score = X @ weights (dot product), then sigmoid-normalized
       to a 0-1 rating after mean-centering.
    5. Fair price via the Normal Equation, theta = (X'X)^-1 X'y, with a bias
       column and pinv for numerical stability.
    6. Price simulation grid: np.polyfit gives the market rate per GB of RAM
       and storage, and np.meshgrid builds the RAM x storage price matrix.

Complexity (n = rows, d = features = 5, g = grid size = 16):
    Time  : O(n*d^2 + d^3) for the Normal Equation (dominant term),
            O(n) for percentiles/polyfit, O(g) for the grid
            -> O(n*d^2) overall, which is effectively linear in n since d is fixed.
    Space : O(n*d) for the feature matrix and its scaled copy.
"""


# ---------------------------------------- Solution -------------------------------------------------------


import numpy as np
import pandas as pd

# 1. Load Dataset
def load_dataset(filepath):
    """
    Load dataset and return the dataframe.
    """
    try:
        # TODO: Load the dataset using Pandas
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return pd.DataFrame()

# 2. Separate Features and Target
def split_features_target(df):
    """
    Split the table into X (Specs) and y (Price).
    """
    feature_cols = [
        "ram_capacity",
        "internal_memory",
        "battery_capacity",
        "primary_camera_rear",
        "rating"
    ]
    # Check if all columns exist
    missing = [col for col in feature_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    # TODO: Select the 'feature_cols' from df and convert to .values (NumPy Matrix)
    X = df[feature_cols].values
    # TODO: Select the "price" column and convert to .values
    y = df["price"].values
    return X, y

# 2.5 Preprocess Features (Crucial Step)
def preprocess_features(X):
    """
    Scale features so they have similar magnitudes.
    Specifically, scale down Battery (5000 -> 50) to match RAM/Storage.
    """
    X_scaled = X.copy()
    # TODO: Scale Battery (Column Index 2) by dividing by 100.
    # We do this once here so ALL functions use the same data range.
    X_scaled[:, 2] = X_scaled[:, 2] / 100
    return X_scaled

# 3. Detect Price Outliers
def detect_price_outliers(prices):
    """
    Find the price range that covers 90% of phones (5th to 95th percentile).
    """
    # TODO: Calculate the 5th percentile
    low = np.percentile(prices, 5)
    # TODO: Calculate the 95th percentile
    high = np.percentile(prices, 95)
    return low, high

# 4. Weighted Smartphone Scoring
def calculate_weighted_score(X_scaled):
    """
    Calculate a 'Tech Score' for each phone using scaled data.
    """
    # Weights: RAM(25%), Storage(20%), Battery(25%), Camera(20%), Rating(10%)
    weights = np.array([0.25, 0.20, 0.25, 0.20, 0.10])

    # TODO: Calculate the weighted score using Matrix Multiplication (Dot Product)
    # Hint: Use np.dot()
    return np.dot(X_scaled, weights)

# 5. Sigmoid Normalization
def sigmoid_normalization(scores):
    """
    Convert raw scores to a 0-1 rating using the Sigmoid function.
    """
    # Center the scores around 0 so sigmoid works best
    centered_scores = scores - np.mean(scores)
    # TODO: Apply the Sigmoid Formula
    # Formula: 1 / (1 + e^(-z)) where z = centered_scores / 10
    return 1 / (1 + np.exp(-(centered_scores / 10)))

# 6. Fair Price Estimation (Normal Equation)
def estimate_fair_price(X_scaled, y):
    """
    Predict fair prices using the Normal Equation (Linear Algebra).
    Formula: theta = (X'X)^-1 X'y
    """
    # Add a column of 1s (Bias term) to X
    ones = np.ones((X_scaled.shape[0], 1))
    X_bias = np.hstack((ones, X_scaled))
    # TODO: Calculate X Transpose (X')
    X_T = np.transpose(X_bias)
    # TODO: Calculate (X'X) -> Matrix Multiplication
    # Hint: Use np.dot()
    xt_x = np.dot(X_T, X_bias)
    # TODO: Calculate Inverse of (X'X)
    # Hint: Use np.linalg.pinv()
    xt_x_inv = np.linalg.pinv(xt_x)
    # TODO: Calculate Theta -> (X'X)^-1 * (X'y)
    theta = np.dot(np.dot(xt_x_inv, X_T), y)
    # TODO: Calculate Predicted Prices -> X_bias * theta
    predicted_prices = np.dot(X_bias, theta)
    return theta, predicted_prices

# 7. Price Simulation using Meshgrid
def simulate_price_grid(df):
    """
    Simulate a price grid for different RAM/Storage combos.
    Uses np.polyfit to find the 'Market Rate' per GB automatically.
    """
    # Calculate 'Price per GB' directly from data (Slope of the line)
    ram_price_per_gb = np.polyfit(df['ram_capacity'], df['price'], 1)[0]
    storage_price_per_gb = np.polyfit(df['internal_memory'], df['price'], 1)[0]
    # Create the grid
    ram_options = np.array([4, 6, 8, 12])
    storage_options = np.array([64, 128, 256, 512])
    # TODO: Generate a Meshgrid for RAM and Storage
    # Hint: Use np.meshgrid()
    RAM_GRID, STORAGE_GRID = np.meshgrid(ram_options, storage_options, indexing="ij")
    # Formula: Base Price + (RAM * RAM_Rate) + (Storage * Storage_Rate)
    base_price = 5000
    # TODO: Calculate the simulated price matrix using the grid variables
    simulated_price = (
        base_price
        + (RAM_GRID * ram_price_per_gb)
        + (STORAGE_GRID * storage_price_per_gb)
    )
    return RAM_GRID, STORAGE_GRID, simulated_price

if __name__ == "__main__":
    try:
        # 1. Load Data
        df = load_dataset("smartphones.csv")
        if not df.empty:
            print(f"1. Data Successfully Loaded: {df.shape[0]} smartphones found.")
            # 2. Split Features (Now uses Explicit Columns)
            X_raw, y = split_features_target(df)
            # Now both 'Score' and 'Price' functions use the same compatible data
            X = preprocess_features(X_raw)
            print(f"   Features Processed & Scaled. Shape: {X.shape}")
            # 3. Outliers
            low, high = detect_price_outliers(y)
            print(f"\n3. Typical Market Price Range: ₹{int(low)} - ₹{int(high)}")
            # 4. Weighted Score (Uses Scaled X)
            scores = calculate_weighted_score(X)
            print(f"\n4. Weighted Hardware Scores (Raw Sum):\n{scores[:5]}")
            # 5. Normalization
            ratings = sigmoid_normalization(scores)
            print(f"\n5. Normalized Spec Ratings (0-1 Scale):\n{np.round(ratings[:5], 2)}")
            # 6. Fair Price Prediction (Uses Scaled X + Pseudo Inverse)
            theta, predicted = estimate_fair_price(X, y)
            print(f"\n6. Estimated Fair Prices (Linear Model):\n{predicted[:5].astype(int)}")
            # 7. Simulation
            print("\n7. Theoretical Price Matrix (RAM vs Storage):")
            RAM, STORAGE, prices = simulate_price_grid(df)
            print(prices.astype(int))

    except Exception as e:
        print(f"\n[!] Error during execution: {e}")
