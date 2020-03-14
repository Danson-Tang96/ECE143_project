import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def show_installsVsratings(df):
    """
    This function will give line plot of the number of installation for different ratings
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    plt.figure(figsize=(10,10))
    g = sns.lineplot(x="Rating", y="Installs",color="green", data=df, ci=0) 
    plt.yscale('log')
    plt.xlabel('Rating',size = 17)
    plt.ylabel('# Installs',size = 17)
    plt.title('Rating vs # Installs',size = 20)
    plt.show()

def show_installsVssize(df):
    """
    This function will give boxplot plot of the number of installation for different app sizes
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    plt.figure(figsize=(10,10))
    g = sns.boxplot(x="Installs", y="Size", data=df, color = 'pink')
    g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")
    plt.title('Installs-Size(kilobyte) ',size = 20)

if __name__ == '__main__':
    pass
