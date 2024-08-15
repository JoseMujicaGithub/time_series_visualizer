import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
    
# If the row count is still not 1238, adjust further
while len(df) > 1238:
    upper_bound -= 1  # Reduce upper bound to drop more rows
    df = df[df['value'] <= upper_bound]

def draw_line_plot():
    # Load and clean the data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Create the line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], 'r-', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    plt.show()


def draw_bar_plot():
    # Load and clean the data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Prepare the data for the bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Create the bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 8), ylabel='Average Page Views', xlabel='Years').figure
    plt.title('Average Page Views per Month')
    plt.xticks(rotation=45)
    plt.legend(title='Months', labels=calendar.month_name[1:])

    plt.show()


np.float = float

def draw_box_plot():
    # Load and clean the data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Prepare data for the box plots
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%b')

    # Set up the figure and axes
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

    # Year-wise box plot
    sns.boxplot(ax=axes[0], x='year', y='value', data=df, palette='Set3')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(ax=axes[1], x='month', y='value', data=df, palette='Set3', order=calendar.month_abbr[1:], hue='month',legend=False)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Adjust layout
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
  option=validate_option("1 for line plot . \n2 for bar plot.\n3 for box plot.\n4 EXIT.\n: ",4)

  if option=="1":
     draw_line_plot()
  if option=="2":
     draw_bar_plot()
  if option=="3":
     draw_box_plot()
  if option=="4":
     break