import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lr_fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(df['Year'].min(), 2050+1)
    y1 = lr_fit1.intercept + x1*lr_fit1.slope
    plt.plot(x1, y1)

    # Create second line of best fit
    lr_fit2 = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    x2 = range(2000, 2050+1)
    y2 = lr_fit2.intercept + x2*lr_fit2.slope
    plt.plot(x2, y2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()