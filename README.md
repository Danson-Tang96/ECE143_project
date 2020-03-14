# ECE143_project Group4 
Analysis of Google Play Store Apps Data
## Members
Mahima Rathore mrathore@eng.ucsd.edu

Amol Sakhale asakhale@eng.ucsd.edu

Zichao Li  zil023@ucsd.edu

Zhe Tang zht002@ucsd.edu
## Problem
The Play Store apps data has enormous potential to drive app-making businesses to success. Actionable insights can be drawn for developers to work on and capture the Android market! In this project, we will perform a rigorous analysis of the Google App store market data & dive deep into aspects that can help developers make their apps successful.

## Dataset
https://www.kaggle.com/lava18/google-play-store-apps
The entire dataset contains two CSV files, googleplaystore.csv of which contains various information like app name, category, rating, number of reviews, size of the app, the total number of installs, price, genres, and few more columns. Another CSV file googleplaystore_user_reviews.csv contains user reviews which are preprocessed and translated to English, whether the sentiment is positive, negative or neutral, sentiment polarity score, sentiment subjectivity score. 

## Proposed Solution and Real-world Application:
The proposed solution in this project proposal is aiming at providing some useful insights for app developers. We will be majorly focusing on two aspects for this project:
Doing a basic exploratory analysis to look for any evident pattern or relationship between the features. 
After understanding patterns between various features, we would like to analyze what makes an app successful. 
We can assume that high ratings, percentage of positive reviews and the number of installs are the factors that define the success of the app. Basically we will analyze various features of the google app store dataset like the reviews, rating, number of installs, price, and category, and find out correlations between them. Some useful correlations and certain assumptions will be set to assess whether the app is successful or not. For example, one criterion could be the minimum number of installs, another could be the minimum rating of the app with a certain number of installs. 
We would also like to do sentiment analysis of the reviews by finding the most common words for positive, negative and neutral reviews, to get more insights about the app. We would also like to focus on a particular app category like gaming and find out more specific correlations for the app’s success. By analyzing the android app market breakdown we would also want to study the relationship of categories with the app’s success.

## Conclusions
We found out relations between different features available in the dataset.  We explored the App category feature and found out how it is related to other features like installs, type of app, and price.  We explored number of installs feature and found out very interesting results.  We found of relation between number of installs and rating and got to know how number number of installs is very low if an app has extremely high rating.  We also analyzed price for different categories. We could find that there were quite a few junk apps whose prices were extremely high. 

## Usage of repository
### Data 
The data folder contains two .csv files which have google play store apps and reviews data. 
We got this data from kaggle. 

### Install dependencies
Install all required packages given in requirement.txt

### Jupyter Notebook
For generating all the plots, run the jupyter notebook.  We have used multiple functions to generate different plots.  These functions are written in respective .py files in pyfiles folder. 

## File structure
The src folder contains all python scripts. The data folder contains all the data needed for the processing.
```
Data Cleaning and show the data
-> location src/eda.py
-> description Functions in this file can clean the invalid value and show details of the data set, such as category, and number of data.
```

```
Get the relationships between different parameter

-> location src/installs.py
-> description Show the relationships between size, rating and installs.

-> location src/pricing.py
-> description Show the relationships between category, size, rating and prices.

-> location src/rating.py
-> description Show the rating across various categories.

-> location src/read_and_show.py
-> description This function will read the data from the csv file and create and return a dataframe from the data.

-> location src/reviews.py
-> description This function will give lineplot between the number of installs and number of reviews.


## Conclusions
We get the relationship between rating, sizes, price and installs and reviews. From the data visulizatoin results, we can see that 
