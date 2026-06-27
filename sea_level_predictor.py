import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit using all data
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, 'r', label='Fit: 1880-2014')

    # Create second line of best fit using data from year 2000
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred_2000 = pd.Series(range(2000, 2051))
    y_pred_2000 = res_2000.slope * x_pred_2000 + res_2000.intercept
    ax.plot(x_pred_2000, y_pred_2000, 'green', label='Fit: 2000-2014')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return
    plt.savefig('sea_level_plot.png')
    return plt.gca()