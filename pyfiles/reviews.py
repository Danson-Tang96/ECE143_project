import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def show1(df):
    g = sns.lineplot(y="Installs",x="Reviews", data=df,size=(10))
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Reviews-Installs ',size = 20)

def show2(df):
    g = sns.lmplot(y="Installs",x="Reviews", data=df,size=10)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Reviews',size = 17)
    plt.ylabel('# Installs',size = 17)
    plt.title('Reviews vs #Installs ',size = 20)

if __name__ == '__main__':
    pass