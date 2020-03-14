import pandas as pd
import scipy.stats as stats

def show_ratings_across_categories(df):
    """
    This function will give distribution of rating for different app categories.
    And also performs one way anova test.
    :param df: Dataframe
    :return: None
    """
    assert isinstance(df, pd.DataFrame)

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
