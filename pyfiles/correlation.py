import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def show1(df):
    corrmat = df.corr()
    p =sns.heatmap(corrmat, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

def show2(df):
    df_copy = df.copy()

    df_copy = df_copy[df_copy.Reviews > 10]
    df_copy = df_copy[df_copy.Installs > 0]

    df_copy['Installs'] = np.log10(df['Installs'])
    df_copy['Reviews'] = np.log10(df['Reviews'])

    sns.lmplot("Reviews", "Installs", data=df_copy)
    ax = plt.gca()
    _ = ax.set_title('Number of Reviews Vs Number of Downloads (Log scaled)')

if __name__ == '__main__':
    pass