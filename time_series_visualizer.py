import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r"fcc-forum-pageviews.csv", index_col = 'date', parse_dates = True)

# Clean data
df = df[(df["value"] > df.value.quantile(0.025)) & (df["value"] < df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    df_line = df.copy()

    fig, ax = plt.subplots(figsize=(17, 6))

    ax.plot(df_line.index, df_line.value, 'r-', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(by=[df.index.year, df.index.month]).mean()
    df_bar.index.names = ['year', 'month']
    df_bar = df_bar.unstack()

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(10,9))
    df_bar.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years', fontsize = 16)
    ax.set_ylabel('Average Page Views', fontsize = 16)

    plt.legend(labels=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'], title='Months', fontsize=16)



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(21, 9))

    sns.boxplot(x='year', y='value', data=df_box, ax=axs[0])
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=axs[1], order=months_order)

    axs[0].set_title("Year-wise Box Plot (Trend)", fontsize=18)
    axs[1].set_title("Month-wise Box Plot (Seasonality)",fontsize=18)

    axs[0].set_xlabel('Year')
    axs[1].set_xlabel('Month')

    axs[0].set_ylabel('Page Views')
    axs[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

if __name__ == '__main__':
    draw_box_plot()
