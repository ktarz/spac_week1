# Import libraries

import pandas as pd
import matplotlib.pyplot as plt

# Read data into dataframe and get info

data = pd.read_csv("DKHousingPricesSample100k.csv")

data.info()

#Show first 10 entries

data.head(10)

#Plotting purchase_price

data['purchase_price'].plot()
data.show()

#Group by region

grouped = data.groupby(by="region", sort=True)
grouped.head()

# Finding mean of purchase_price based on region

grouped['purchase_price'].mean()

# Can run it, but for some reason it hits a infinite loop of something causing the data to not be shown
# To be fixed

import matplotlib.pyplot as plt

grouped.plot(kind='bar', x='region', y='purchase_price')
grouped.show()

# Group by house_type
# Finding mean purchase_price based on house_type

grouped_house_type = data.groupby(by='house_type', sort=True)
grouped_house_type['purchase_price'].mean()

# Group by both region and house type
# Finding mean based on this

grouped_sort_mixed = data.groupby(['region','house_type'], sort=True)
grouped_sort_mixed['purchase_price'].mean()
