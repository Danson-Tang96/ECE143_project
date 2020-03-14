import pandas as pd
import numpy as np

def read_and_show():
    """
    This function will read the data from the csv file and create and return a dataframe from the data
    :param df: None
    :return: None
    """
    df = pd.read_csv('data/googleplaystore.csv') #dataframe

    df.drop_duplicates(subset='App', inplace=True)
    df = df[df['Android Ver'] != np.nan]
    df = df[df['Android Ver'] != 'NaN']
    df = df[df['Installs'] != 'Free']
    df = df[df['Installs'] != 'Paid']

    df.sample(4)
    print(df.count())
    print(df['Category'].unique())
    
    return df

def clean_data(df):
    """
    This function will will perform different required cleaning operations on different columns.
    :param df: Dataframe
    :return df: Dataframe
    """
    assert isinstance(df, pd.DataFrame)

    # Cleaning of the data
    df['Installs'] = df['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)
    df['Installs'] = df['Installs'].apply(lambda x: x.replace(',', '') if ',' in str(x) else x)
    df['Installs'] = df['Installs'].apply(lambda x: int(x))
    print(type(df['Installs'].values))

    #Size : Remove 'M', Replace 'k' and divide by 10^-3
    df['Size'] = df['Size'].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
    df['Size'] = df['Size'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
    df['Size'] = df['Size'].apply(lambda x: str(x).replace(',', '') if 'M' in str(x) else x)
    df['Size'] = df['Size'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
    df['Size'] = df['Size'].apply(lambda x: float(x))
    df['Installs'] = df['Installs'].apply(lambda x: float(x))

    df['Price'] = df['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
    df['Price'] = df['Price'].apply(lambda x: float(x))

    df['Reviews'] = df['Reviews'].apply(lambda x: int(x))

    return df

if __name__ == '__main__':
    pass
