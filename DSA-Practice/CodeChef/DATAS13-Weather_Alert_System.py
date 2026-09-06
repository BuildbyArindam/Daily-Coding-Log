"""
Problem: Weather Alert System Project (DATAS13)
Platform: CodeChef
Link: https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ03/problems/DATAS13
Date Solved: 2026-09-06
Difficulty: Medium
Topics: NumPy, Pandas, Data Cleaning, Boolean Masking, Array Clipping, Fancy Indexing

Approach:
    - Load raw sensor readings via pandas.read_csv, flatten to a 1D NumPy array.
    - Build a boolean mask to flag heat alerts (>40°C).
    - Sanitize faulty sensor data: negative readings -> 0 (np.where),
      then clip all values to a safe [0, 45] range (np.clip).
    - Audit specific sensor indices (fancy indexing) post-cleaning.
    - Convert cleaned Celsius readings to Fahrenheit for dashboard display.

Time Complexity:  O(n) — every step is a single-pass vectorized NumPy operation
                  over the n sensor readings (load, mask, where, clip, convert).
Space Complexity: O(n) — one or two additional arrays of size n are created
                  per transformation step (no recursion/extra structures).
"""


# ----------------------- Solution ----------------------------


import numpy as np
import pandas as pd


# 1. Loading Weather Data
def load_weather_data(filename):
    """
    Load data using Pandas read_csv.
    """
    try:
        # TODO: Load the CSV file
        df = pd.read_csv(filename)
        
        # TODO: Convert the DataFrame to a 1D NumPy array (flattened)
        return df.to_numpy().flatten()
        
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return np.array([])


# 2. Identify Extreme Heat Alerts
def detect_heat_alerts(temps):
    """ Return True for any sensor reading above 40°C. """
    
    # TODO: Generate a boolean mask where temperatures exceed 40
    return temps > 40


# 3. Fix Sensor Errors
def replace_negative_values(temps):
    """
    Replace negative values with 0.
    """
    # TODO: Use a NumPy function to replace values < 0 with 0
    return np.where(temps < 0, 0, temps)


# 4. Enforce Safe Limits
def clip_temperature_range(temps, low=0, high=45):
    """
    Clip values to a max of 45°C.
    """
    # TODO: Restrict the array values to the [low, high] interval
    return np.clip(temps, low, high)


# 5. Monitor Critical Infrastructure
def monitor_critical_zones(temps):
    """
    Check specific high-interest zones:
    - Index 4: Had a glitch (-5) -> Should now be 0
    - Index 9: Was extreme (60) -> Should now be 45
    - Index 11: Normal value (15)
    """
    # TODO: Extract readings from the specific indices mentioned above
    result = temps[[4, 9, 11]]
    return result


# 6. Convert to Fahrenheit
def convert_to_fahrenheit(temps):
    """ Convert Celsius to Fahrenheit. """
    # TODO: Apply the standard conversion formula
    return (temps * 1.8) + 32


if __name__ == "__main__":

    filename = 'weather_data.csv'
    temps = load_weather_data(filename)
    
    if temps.size > 0:
        print(f"Data Loading:")
        print(f"Successfully loaded {len(temps)} records.")
        print(f"Raw Data: {temps}\n")

        alerts = detect_heat_alerts(temps)
        if alerts is not None:
            print(f"Heatwave Detection (>40°C):")
            print(f"Alert Mask: {alerts.astype(int)}") 
            print(f"Result: Found {alerts.sum()} sensors reporting critical heat.\n")
        
        cleaned = replace_negative_values(temps)
        if cleaned is not None:
            print(f"Sensor Glitch Correction:")
            print(f"Replaced negative values with 0.")
            print(f"Cleaned Data: {cleaned}\n")

            clipped = clip_temperature_range(cleaned)
            if clipped is not None:
                print(f"Safety Limit Enforcement:")
                print(f"Clipped values > 45°C to strictly 45.")
                print(f"Safe Data: {clipped}\n")

                critical_zones = monitor_critical_zones(clipped)
                if critical_zones is not None:
                    print(f"Critical Zone Audit:")
                    print(f"Server Room (Idx 4), Battery (Idx 9), Hall (Idx 11)")
                    print(f"Readings: {critical_zones}\n")

                fahrenheit = convert_to_fahrenheit(clipped)
                if fahrenheit is not None:
                    print(f"Dashboard Display Conversion:")
                    print(f"Data in Fahrenheit: {fahrenheit}")
