# Air Quality Index Prediction using python

# -> PM2.5, PM10
# -> NO,NO2
# -> NH3
# -> CO
# -> So2
# -> O3
# -> Benzene,Toluene,Xylene

# importing necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sna
from warnings import filterwarnings
filterwarnings('ignore')

df = pd.read_csv('air quality data.csv')
df.head()  # shows top 5rows

# shape - rows and columns
df.shape

# information
df.info()

# to know duplicate values
df.duplicated().sum()

# to check missing values
df.isnull().sum()

# drop the rows where 'AQI' has missing values
df.dropna(subset=['AQI'], inplace=True)

df.isnull().sum().sort_values(ascending=False)

df.shape

# Summary of statistics in the dataset
df.describe().T

# percentage of the null values
null_value_percentage = (
    df.isnull().sum()/df.isnull().count()*100).sort_values(ascending=False)

# key consideration
# -> Xylene has the highest percentage of missing values-61.86%
# -> Pm10 and NH3 28-26%
