import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

sales = pd.read_csv( 'https://raw.githubusercontent.com/ine-rmotr-curriculum/FreeCodeCamp-Pandas-Real-Life-Example/master/data/sales_data.csv', parse_dates=['Date'])

sales.head()

sales['Customer_Age'].mean()

sales['Customer_Age'].plot(kind='kde', figsize=(14,6))
sales['Customer_Age'].plot(kind='box', vert=False, figsize=(14,6))  #two different graphs 'hist'
 
sales['Year'].value_counts() #all rows with each year  

sales.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=(6,6))

sales['Revenue'] += 50 #change every revenue

sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0] #how many sales in canada and france

sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0] #bike sales from canada