import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import legend
import seaborn as sns

def show_top_categories(df):
    """
    This function will take dataframe as a input and give us Barplot of the top 4 app categories
    according to total number of apps in the category
    :param df: dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    number_of_apps_in_category = df['Category'].value_counts().sort_values(ascending=True)
    print(number_of_apps_in_category)
    # These are the percentage values for top 4 categories
    data = [4.35, 8.56, 9.93, 19]
    labels = ['BUSINESS','TOOLS','GAME','FAMILY']
    plt.figure(figsize=(10,10))
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Categories',size = 15)
    plt.ylabel('Number of Apps (%)',size = 15)
    plt.title('Top Four Categories with highest marketshare',size = 20)
    plt.bar(range(len(data)), data,color='#00b386') 
    plt.show()

def show_categories_count(df):
    """
    This function will take a dataframe as a input and will give countplot of the all App categories
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    order_category = df['Category'].value_counts().iloc[:15].index
    plt.figure(figsize=(10,10))
    g = sns.countplot(y="Category",data=df, color='#ff4d4d',order = order_category)
    plt.title('Total # of apps in each Category',size = 20)


def show_categories_freeVspaid(df):
    """
    This function will give us the count plot for top 5 categories with Free vs Paid comparison
    :param df: Dataframe
    :return:None
    """
    assert isinstance(df, pd.DataFrame)

    order_category = df['Category'].value_counts().iloc[:5].index
    plt.figure(figsize=(10,10))
    g = sns.countplot(y="Category",data=df,order = order_category,hue =df['Type'],palette="PuRd",saturation = 0.9)
    plt.title('Free vs Paid Apps in Top 5 Categories',size = 20)
    plt.setp(g.get_legend().get_texts(), fontsize='18') # for legend text
    plt.setp(g.get_legend().get_title(), fontsize='18') # for legend title


def show_freeVspaid(df):
    """
    This function will give pie chart with contribution of free and paid apps in data
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    # Data to plot
    labels =df['Type'].value_counts(sort = True).index
    sizes = df['Type'].value_counts(sort = True)
    legend.rcParams['font.size'] = 20.0
    colors = ["#ffb3ff","#cc0099"]
    explode = (0.1,0)  # explode 1st slice

    plt.figure(figsize=(8,8))
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=270,)
    plt.title('Apps Distribution: Free vs Paid (in %)',size = 15)
    plt.show()

def show_installations_categories(df):
    """
    This function will give Bar plot of the number of installation of different categories
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    ordered_cat = df[['Installs', 'Category']].groupby('Category').mean().sort_values('Installs',ascending=False).iloc[:15].index
    plt.figure(figsize=(10,10))
    g = sns.barplot(x="Installs", y="Category", data=df, capsize=.6, color = '#66d9ff', order= ordered_cat, ci=None)
    plt.title('#Installations in each Category',size = 20)

def show_installations_freeVspaid(df):
    """
    This function will give Bar plot of the number of installation of different categories with free vs paid contribution
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    ordered_cat = df[['Installs', 'Category']].groupby('Category').mean().sort_values('Installs',ascending=False).iloc[:5].index
    plt.figure(figsize=(10,10))
    g = sns.barplot(x="Installs",y="Category",data=df, order= ordered_cat, ci=None,hue = df['Type'],palette="YlGnBu",saturation = 0.8)
    plt.title('Free vs Paid App-Installations in each Category',size = 20)

    plt.setp(g.get_legend().get_texts(), fontsize='18') # for legend text
    plt.setp(g.get_legend().get_title(), fontsize='18') # for legend title

def get_top_installed_apps(df):
    """
    This function will give the dataframe having apps with highest number of installs
    :param df: Dataframe
    :return: Dataframe
    """
    top_10_apps_by_inst = df.sort_values(by=['Installs'], ascending=False)
    temp = top_10_apps_by_inst[['App', 'Installs','Category', 'Type']][:20]
    temp = temp.sort_values(by=['Category'])
    temp.loc[temp.Installs==1.000000e+09, 'Installs']='1 Billion'
    return temp

def get_top_installed_paid_apps(df):
    """
    This function will give the dataframe having top paid apps with highest number of installs.
    :param df: Dataframe
    :return: Dataframe
    """
    top_paid_Apps = df.loc[df['Type'] == 'Paid'].sort_values(by=['Installs'], ascending=False)
    temp = top_paid_Apps[['App', 'Installs', 'Category', 'Type']][:15]
    temp.loc[temp.Installs==1000000, 'Installs']='1 Million'
    temp.loc[temp.Installs==10000000, 'Installs']='10 Million'
    temp = temp.sort_values(by=['Category'])

    return temp


if __name__ == '__main__':
    pass