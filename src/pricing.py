import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def show_priceVsrating(df):
    """
    This function will give the jointplot of price and rating
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    paid_apps = df[df.Price>0]
    plt.figure(figsize = (10,10))
    p = sns.jointplot( "Price", "Rating", paid_apps,size = 8, color = 'red')


def show_priceVssize(df):
    """
    This function will give the jointplot of price and size
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    paid_apps = df[df.Price>0]
    p = sns.jointplot( "Price", "Size", paid_apps, size = 8)

def show_priceVscategory(df):
    """
    This function will give the plot of price for different app categories
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    subset_df = df[df.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY', 'MEDICAL', 'TOOLS', 'FINANCE', 'LIFESTYLE','BUSINESS'])]
    sns.set_style('darkgrid')
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8)
    p = sns.stripplot(x="Price", y="Category", data=subset_df, jitter=True, linewidth=1, color = '#e6004c')
    plt.xlabel('Price',size =15)
    plt.ylabel('Category',size = 15)
    title = ax.set_title('App Pricing Trend across Categories',size = 20)

def show_priceVscategory_filtered(df):
    """
    This function will give the plot of price for different app categories after filtering junk apps
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    subset_df = df[df.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY', 'MEDICAL', 'TOOLS', 'FINANCE','LIFESTYLE','BUSINESS'])]
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8)
    subset_df_price = subset_df[subset_df.Price<100]
    p = sns.stripplot(x="Price", y="Category", data=subset_df_price, jitter=True, linewidth=1, color = 'violet')
    title = ax.set_title('App pricing trend across categories - after filtering for junk apps')

def show_freeVspaid_distri_categories(df):
    """
    This function will give the piechart showing free vs paid apps in different app categories
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    new_df = df.groupby(['Category', 'Type']).agg({'App' : 'count'}).reset_index()
    print(new_df)

    outer_group_names = ['GAME', 'FAMILY', 'MEDICAL', 'TOOLS']
    outer_group_values = [len(df.App[df.Category == category]) for category in outer_group_names]

    a, b, c, d=[plt.cm.Reds, plt.cm.Greys, plt.cm.Greens, plt.cm.Oranges]

    inner_group_names = ['Paid', 'Free'] * 4
    inner_group_values = []

    for category in outer_group_names:
        for t in ['Paid', 'Free']:
            x = new_df[new_df.Category == category]
            try:
                inner_group_values.append(int(x.App[x.Type == t].values[0]))
            except:
                inner_group_values.append(0)

    explode = (0.025,0.025,0.025,0.025)
    # First Ring (outside)
    fig, ax = plt.subplots(figsize=(10,10))
    ax.axis('equal')
    mypie, texts, _ = ax.pie(outer_group_values, radius=1.2, labels=outer_group_names, autopct='%1.1f%%', pctdistance=1.1,
                                    labeldistance= 0.75,  explode = explode, colors=[a(0.6), b(0.6), c(0.6), d(0.6)], textprops={'fontsize': 16})
    plt.setp( mypie, width=0.5, edgecolor='black')
    
    # Second Ring (Inside)
    mypie2, _ = ax.pie(inner_group_values, radius=1.2-0.5, labels=inner_group_names, labeldistance= 0.7, 
                    textprops={'fontsize': 12}, colors = [a(0.4), a(0.2), b(0.4), b(0.2), c(0.4), c(0.2), d(0.4), d(0.2)])
    plt.setp( mypie2, width=0.5, edgecolor='black')
    plt.margins(0,0)
    
    # show it
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    pass
