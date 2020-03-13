# ECE143_project Group4 
Analysis of Google Play Store Apps Data
## Members
Mahima Rathore mrathore@eng.ucsd.edu

Amol Sakhale amolsakhale99@gmail.com

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

## Libraries Used
The user should import all the libararies listed below in order to run the project. You can see the libraries used in requirements.txt

## Conclusions
We get the relationship between rating, sizes, price and installs and reviews. From the data visulizatoin results, we can see that 
