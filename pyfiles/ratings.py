import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def show1(df):
    import scipy.stats as stats

    f = stats.f_oneway(df.loc[df.Category == 'BUSINESS']['Rating'].dropna(), 
                    df.loc[df.Category == 'FAMILY']['Rating'].dropna(),
                    df.loc[df.Category == 'GAME']['Rating'].dropna(),
                    df.loc[df.Category == 'PERSONALIZATION']['Rating'].dropna(),
                    df.loc[df.Category == 'LIFESTYLE']['Rating'].dropna(),
                    df.loc[df.Category == 'FINANCE']['Rating'].dropna(),
                    df.loc[df.Category == 'EDUCATION']['Rating'].dropna(),
                    df.loc[df.Category == 'MEDICAL']['Rating'].dropna(),
                    df.loc[df.Category == 'TOOLS']['Rating'].dropna(),
                    df.loc[df.Category == 'PRODUCTIVITY']['Rating'].dropna()
                    )

    print(f)
    print('\nThe p-value is extremely small, hence we reject the null hypothesis in favor of the alternate hypothesis.\n')

    groups = df.groupby('Category').filter(lambda x: len(x) > 286).reset_index()
    array = groups['Rating'].hist(by=groups['Category'], sharex=True, figsize=(20,20))

if __name__ == '__main__':
    pass