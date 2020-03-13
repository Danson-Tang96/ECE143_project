import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def show1(df):
    plt.figure(figsize=(10,10))
    #plt.scatter( x=df['Rating'], y=df['Installs'] , color = 'orange')
    g = sns.lineplot(x="Rating", y="Installs",color="green", data=df, ci=0) 
    plt.yscale('log')
    plt.xlabel('Rating',size = 17)
    plt.ylabel('# Installs',size = 17)
    plt.title('Rating vs # Installs',size = 20)
    plt.show()

def show2(df):
    plt.figure(figsize=(10,10))
    g = sns.boxplot(x="Installs", y="Size", data=df, color = 'pink')
    g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")
    plt.title('Installs-Size(kilobyte) ',size = 20)

if __name__ == '__main__':
    pass