import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def show_reviewsVsinstalls_lineplot(df):
    """
    This function will give lineplot between the number of installs and number of reviews
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    g = sns.lineplot(y="Installs",x="Reviews", data=df,size=10)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Reviews-Installs ',size = 20)

def show_reviewsVsinstalls_lmplot(df):
    """
    This function will give lmplot between the number of installs and number of reviews
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

    g = sns.lmplot(y="Installs",x="Reviews", data=df,size=10)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Reviews',size = 17)
    plt.ylabel('# Installs',size = 17)
    plt.title('Reviews vs #Installs ',size = 20)

if __name__ == '__main__':
    pass
