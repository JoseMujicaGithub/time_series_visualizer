import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Clean data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
df = df.reset_index()
    
while len(df) > 1238:
    upper_bound -= 1 
    df = df[df['value'] <= upper_bound]

def draw_line_plot():

    fig=plt.figure(figsize=(15, 5))
    plt.plot(df['date'], df['value'], 'r-', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.show()

def draw_bar_plot():

    # Copy and modify data for monthly bar plot
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df_bar = df.copy()
    df_bar['month'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()
    
    df_bar_pivot = df_bar.pivot_table(values='value', index='year', columns='month', aggfunc='mean')


    fig = df_bar_pivot.plot(kind='bar', figsize=(10, 8), ylabel='Average Page Views', xlabel='Years')
    plt.title('Average Page Views per Month')
    plt.xticks(rotation=45)
    plt.legend(title='Months')
    plt.show()


np.float = float

def draw_box_plot():
    # Load the data
    
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    
    # Filter outliers (keep only the data between the 2.5th and 97.5th percentiles)
    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)
    df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
    
    # If the row count is still not 1238, adjust further
    while len(df) > 1238:
        upper_bound -= 1  # Reduce upper bound to drop more rows
        df = df[df['value'] <= upper_bound]
    
    # Prepare data for year-wise box plot
    df['year'] = df.index.year

    # Prepare data for month-wise box plot using abbreviated month names
    df['month'] = df.index.month
    df['month_abbr'] = df['month'].apply(lambda x: calendar.month_abbr[x])

    # Custom color palettes
    #year_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  
    #month_colors = ['#e377c2', '#ff7f0e', '#bcbd22', '#17becf', 
    #                '#2ca02c', '#1f77b4', '#98df8a', '#17becf', 
    #                '#7f7f7f', '#9467bd', '#c49c94', '#f7b6d2']  

    # Set up the figure and axes
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
    
    # Year-wise box plot with colors
    sns.boxplot(ax=axes[0], x='year', y='value', data=df, palette='Set2', hue='year', legend=False) #use palette=year_colors for custom colors
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot with colors and abbreviated month names
    sns.boxplot(ax=axes[1], x='month_abbr', y='value', data=df, hue='month_abbr', legend=False,
                palette='Set3', 
                order=calendar.month_abbr[1:])  # Exclude the first empty string for month names
                #use palette=month_colors for custom colors
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    # Show the plots
    plt.tight_layout()
    plt.show()


def validate_option(message=": ",max_option=1):
  while True:
    option_=input(message)
    try: 
      if int(option_)<=max_option and int(option_)>0:
        break
    except:
      print("===Input a valid option===")
  return option_

while True:
  print("Chose your chart from the menu:")
  option=validate_option("1 for line plot. \n2 for bar plot.\n3 box plot.\n4 EXIT.\n: ",4)

  if option=="1":
     draw_line_plot()
  if option=="2":
     draw_bar_plot()
  if option=="3":
     draw_box_plot()
  if option=="4":
     break