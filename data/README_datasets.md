<font size=7> Kaggle Dataset Notes </font><br/>
<font size=2> Revised on 01.04.2020 </font><br/>

<hr style="border: solid rgb(0,0,0) 0.0px; background-color: rgb(0,0,0);height: 5.0px;"/>

# Sberbank Russian Housing Market

[sberbank-russian-housing-market](https://www.kaggle.com/c/sberbank-russian-housing-market/data)

The aim of this competition is to _predict the sale price of each property_. The target variable is called price_doc in train.csv.

The training data is from August 2011 to June 2015, and the test set is from July 2015 to May 2016. The dataset also includes information about overall conditions in Russia's economy and finance sector, so you can focus on generating accurate price forecasts for individual properties, without needing to second-guess what the business cycle will do.

Update: please see the pinned discussion thread for some optional extra data, resolving an issue with some GIS features.

---

# Rossmann Store Sales

[rossmann-store-sales](https://www.kaggle.com/c/rossmann-store-sales/data)

<font color='red' size=2>Requires time-series analysis and prediction (_ie_ 'forecasting')</font>

You are provided with historical sales data for 1,115 Rossmann stores. The task is to forecast the "Sales" column for the test set. Note that some stores in the dataset were temporarily closed for refurbishment.

---

# US Health Insurance Dataset: 

[ushealthinsurancedataset](https://www.kaggle.com/teertha/ushealthinsurancedataset)

* This dataset contains 1338 rows of insured data, where the Insurance charges are given against the following attributes of the insured: Age, Sex, BMI, Number of Children, Smoker and Region. There are no missing or undefined values in the dataset.
* This relatively simple dataset should be an excellent starting point for EDA, Statistical Analysis and Hypothesis testing and training Linear Regression models for _predicting Insurance Premium Charges._

* Proposed Tasks:
    * Exploratory Data Analytics
    * Statistical hypothesis testing
    * Statistical Modeling
    * Linear Regression
---
    
# New York City Taxi Fare Prediction
[new-york-city-taxi-fare-prediction](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/data)

<font color='red' size=3>Data is currently too large, ca. 6 GB</font>


File descriptions

* train.csv - Input features and target fare_amount values for the training set (about 55M rows ca. 6GB!).
* test.csv - Input features for the test set (about 10K rows). Your goal is to predict fare_amount for each row.
* sample_submission.csv - a sample submission file in the correct format (columns key and fare_amount). This file 'predicts' fare_amount to be $11.35 for all rows, which is the mean fare_amount from the training set.
* Target - fare_amount - float dollar amount of the cost of the taxi ride. This value is only in the training set; this is what you are predicting in the test set and it is required in your submission CSV


--- 


# Santander Value Prediction Challenge

[santander-value-prediction-challenge](https://www.kaggle.com/c/santander-value-prediction-challenge/data)

<font color='red' size=3> Data is 5000$\times$5000 <br/>
Column names are currently gibberish, `ID,48df886f9,0deb4b6a8,34b15f335,...` <br/>
</font>

You are provided with an anonymized dataset containing numeric feature variables, the numeric target column, and a string ID column.

The task is to _predict the value of target column_ in the test set.

File descriptions

* train.csv - the training set
* test.csv - the test set
* sample_submission.csv - a sample submission file in the correct format

---

# Zillow Prize: Zillow’s Home Value Prediction (Zestimate)

[zillow-prize-1](https://www.kaggle.com/c/zillow-prize-1/data)

In this competition, Zillow is asking you to _predict the log-error between their Zestimate and the actual sale price_, given all the features of a home. The log error is defined as
logerror=log(Zestimate)−log(SalePrice)

and it is recorded in the transactions file train.csv. In this competition, you are going to _predict the logerror for the months in Fall 2017_. Since all the real estate transactions in the U.S. are publicly available, we will close the competition (no longer accepting submissions) before the evaluation period begins. 

* You are asked to predict 6 time points for all properties: 
    * October 2016 (201610), 
    * November 2016 (201611), 
    * December 2016 (201612), 
    * October 2017 (201710), 
    * November 2017 (201711),
    * December 2017 (201712).

---

# Predict Future Sales

[competitive-data-science-predict-future-sales](https://www.kaggle.com/c/competitive-data-science-predict-future-sales/data)

You are provided with daily historical sales data. The task is to _forecast the total amount of products sold in every shop_ for the test set. Note that the list of shops and products slightly changes every month. Creating a robust model that can handle such situations is part of the challenge.


## Notes: 
* some time-series analysis
* Russian text

---

# Supermarket sales

[supermarket-sales](https://www.kaggle.com/aungpyaeap/supermarket-sales)
    
* some time-series analysis: _predict the sales for 3 supermarkets fur how long?_
        
Then we choose many base models, cross-validate them on the data before stacking/ensembling them. The key here is to make the (linear) models robust to outliers. This improved the result both on LB and cross-validation.

---

# Costa Rican Household Poverty Level Prediction

[costa-rican-household-poverty-prediction](https://www.kaggle.com/c/costa-rican-household-poverty-prediction/data)

_Predict the target_ 

Classification

* {train|test}.csv - the training set 
    * This is the main table, broken into two files for Train (with a Target column) and Test (without the Target column). 

* Target - the target is an ordinal variable indicating groups of income levels.
    1 = extreme poverty
    2 = moderate poverty
    3 = vulnerable households
    4 = non vulnerable households




