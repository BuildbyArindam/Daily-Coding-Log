"""
Problem   : Iris 3D Mapper Project
Platform  : CodeChef (Data Analysis & Visualization Projects, DATAS23)
Link      : https://www.codechef.com/practice/course/data-analysis-visualization-projects/DATASPRJ05/problems/DATAS23
Difficulty: Medium
Topics    : Data Visualization, Pandas, Matplotlib, 3D Plotting
Date      : 2026-10-03

Approach:
    Load the Iris CSV with pandas, then produce three plots with Matplotlib
    (Agg backend, so no GUI is needed):
      1. 2x2 grid of histograms for the four numeric features.
      2. 3D scatter of SepalLength/SepalWidth/PetalLength, coloured by species,
         with a dashed line joining the per-species mean points.
      3. Filled contour map (tricontourf) of PetalWidth over
         SepalLength x SepalWidth, with the raw points overlaid.

Complexity (n = number of rows, k = number of species, k is constant):
    Time : O(n log n), dominated by the Delaunay triangulation inside
           tricontourf. Loading, groupby, histograms and scatter are O(n).
    Space: O(n) for the DataFrame and plot data.
"""


# ---------------------------------------- Solution ------------------------------------------------------


import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
# Force Matplotlib to work without GUI
matplotlib.use("Agg")

# 1. Load Iris Data
def load_iris_data(filepath):
    """
    Load the Iris dataset from CSV.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)
        print("Iris dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

# 2. Feature Distribution (Histograms)
def plot_feature_distributions(df):
    """
    Create and save a 2x2 grid of histograms to show data distribution.
    Visualizing feature distributions using histograms.
    """
    # Create a figure with 2 rows and 2 columns
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("Iris Feature Distributions")
    # Row 0, Col 0: SepalLengthCm
    # color: skyblue, number of bins: 15, edgecolor: black
    axes[0, 0].hist(
        df['SepalLengthCm'],
        bins=15,
        color='skyblue',
        edgecolor='black'
    )
    axes[0, 0].set_title('Sepal Length (Cm)')
    # Row 0, Col 1: SepalWidthCm
    # color: salmon, number of bins: 15, edgecolor: black
    axes[0, 1].hist(
        df['SepalWidthCm'],
        bins=15,
        color='salmon',
        edgecolor='black'
    )
    axes[0, 1].set_title('Sepal Width (Cm)')
    # Row 1, Col 0: PetalLengthCm
    # color: lightgreen, number of bins: 15, edgecolor: black
    axes[1, 0].hist(
        df['PetalLengthCm'],
        bins=15,
        color='lightgreen',
        edgecolor='black'
    )
    axes[1, 0].set_title('Petal Length (Cm)')
    # Row 1, Col 1: PetalWidthCm
    # color: gold, number of bins: 15, edgecolor: black
    axes[1, 1].hist(
        df['PetalWidthCm'],
        bins=15,
        color='gold',
        edgecolor='black'
    )
    axes[1, 1].set_title('Petal Width (Cm)')
    plt.tight_layout()
    # Save the plot
    output_file = "iris_distributions.png"
    plt.savefig(output_file)
    print(f"Distributions plot saved to {output_file}")

# 3. 3D Scatter + Line Plot
def plot_3d_clusters(df):
    """
    Visualize species in 3D space and connect their averages with a line.
    """
    # Size of the figure
    fig = plt.figure(figsize=(10, 8))
    # Create 3D axes using projection = "3d"
    # Number of rows = 1, Number of columns = 1, index = 1
    ax = fig.add_subplot(111, projection="3d")
    # Colors for the species
    colors = {
        'Iris-setosa': 'red',
        'Iris-versicolor': 'green',
        'Iris-virginica': 'blue'
    }
    # Part A: 3D Scatter Plot
    # Loop through each species group to plot points
    for species, group in df.groupby('Species'):
        # Create the Scatter Plot
        ax.scatter(
            # Map the 3 axes to SepalLength, SepalWidth, PetalLength
            group['SepalLengthCm'],  # X Axis
            group['SepalWidthCm'],   # Y Axis
            group['PetalLengthCm'],  # Z Axis
            # Apply the color based on species
            c=colors.get(species, 'black'),
            # Mark the label for legend as "species"
            label=species,
            # Set the size of points to 50 and transparency to 0.6
            s=50,
            alpha=0.6
        )
    # Part B: 3D Line Plot (Evolutionary Path)
    # Calculate the MEAN (average) of numerical columns grouped by Species
    numeric_cols = [
        'SepalLengthCm',
        'SepalWidthCm',
        'PetalLengthCm',
        'PetalWidthCm'
    ]
    means = df.groupby('Species')[numeric_cols].mean()
    # Draw a line connecting the centers (means) of the clusters
    ax.plot(
        # Map the 3 axes to the means of SepalLength, SepalWidth, PetalLength
        means['SepalLengthCm'],  # X axis
        means['SepalWidthCm'],   # Y axis
        means['PetalLengthCm'],  # Z axis
        # Set color to black
        color='black',
        # Set line width to 3
        linewidth=3,
        # Set line style to dashed
        linestyle='--',
        # Set label for legend as "Cluster Center Path"
        label='Cluster Center Path'
    )
    # Labels of the axes
    ax.set_title("3D Species Clusters & Trends")
    ax.set_xlabel("Sepal Length (Cm)")
    ax.set_ylabel("Sepal Width (Cm)")
    ax.set_zlabel("Petal Length (Cm)")
    ax.legend()
    # Save the plot
    output_file = "iris_3d_scatter.png"
    plt.savefig(output_file, dpi=150)
    print(f"3D Scatter plot saved to {output_file}")

# 4. Plot Filled Contour Map
def plot_contour_map(df):
    """
    Create a filled contour map to represent elevation using Petal Width.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    # Define X, Y, Z for the map
    # Map Sepal Length to X axis and Sepal Width to Y axis
    x = df['SepalLengthCm']
    y = df['SepalWidthCm']
    # Use Petal Width as the "elevation" (Z axis)
    z = df['PetalWidthCm']
    # Create the Filled Contour Map
    # Number of levels = 14, colormap = 'inferno'
    contour = ax.tricontourf(
        x,
        y,
        z,
        levels=14,
        cmap='inferno'
    )
    # Adding a color bar
    cbar = plt.colorbar(contour)
    cbar.set_label('Petal Width (Elevation)')
    # Overlay the original points so we can see the data density
    # Color of points: black, size: 10, transparency: 0.3, label: 'Data Points'
    ax.scatter(
        x,
        y,
        c='black',
        s=10,
        alpha=0.3,
        label='Data Points'
    )
    ax.set_title("Topological Map of Petal Width")
    ax.set_xlabel("Sepal Length (Cm)")
    ax.set_ylabel("Sepal Width (Cm)")
    ax.legend()
    # Save the plot
    output_file = "iris_contour_map.png"
    plt.savefig(output_file)
    print(f"Contour map saved to {output_file}")

if __name__ == "__main__":
    # Load Data
    df = load_iris_data("iris.csv")
    if not df.empty:
        # 1. Visualization: Histograms
        print("\nGenerating Histograms...")
        plot_feature_distributions(df)
        # 2. Visualization: 3D Scatter
        print("\nGenerating 3D Scatter Plot...")
        plot_3d_clusters(df)
        # 3. Visualization: Contour Map
        print("\nGenerating Contour Map...")
        plot_contour_map(df)
