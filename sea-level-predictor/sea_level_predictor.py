import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit (all data)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_all = np.arange(df["Year"].min(), 2051)
    y_all = res_all.intercept + res_all.slope * x_all
    plt.plot(x_all, y_all)

    # Create second line of best fit (year 2000 onwards)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )
    x_recent = np.arange(2000, 2051)
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    plt.plot(x_recent, y_recent)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
