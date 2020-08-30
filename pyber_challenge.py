# -*- coding: utf-8 -*-
"""PyBer_Challenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X1stGt4D8vKuUbL2Oj0HySmocVWGltDQ

# Pyber Challenge
"""

from google.colab import drive
drive.mount('/content/drive')

"""### 4.3 Loading and Reading CSV files"""

# Commented out IPython magic to ensure Python compatibility.
# Add Matplotlib inline magic command
# %matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = "/content/drive/My Drive/Colab Notebooks/PyBer_Analysis/Resources/city_data.csv"
ride_data_to_load = "/content/drive/My Drive/Colab Notebooks/PyBer_Analysis/Resources/ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)

"""### Merge the DataFrames"""

# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])
# Display the data table for preview
pyber_data_df.head()

"""## Deliverable 1: Get a Summary DataFrame"""

#  1. Get the total rides for each city type
total_rides = pyber_data_df.groupby(['type']).count()['ride_id']
total_rides

# 2. Get the total drivers for each city type
total_drivers = city_data_df.groupby(['type']).sum()['driver_count']
total_drivers

#  3. Get the total amount of fares for each city type
total_fares = pyber_data_df.groupby(['type']).sum()['fare']
total_fares

#  4. Get the average fare per ride for each city type. 
avg_fare_ride = pyber_data_df.groupby(['type']).mean()['fare']
avg_fare_ride

# 5. Get the average fare per driver for each city type. 
avg_fare_driver = pyber_data_df.groupby(['type']).sum()['fare'] / total_drivers
avg_fare_driver

#  6. Create a PyBer summary DataFrame. 
pyber_summary_df = pd.DataFrame({
    'Total Rides': total_rides,
    'Total Drivers': total_drivers,
    'Total Fares': total_fares,
    'Avg. Fare per Ride': avg_fare_ride,
    'Avg. Fare per Driver': avg_fare_driver
})

pyber_summary_df

#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None
pyber_summary_df

#  8. Format the columns.
pyber_summary_df['Total Rides'] = pyber_summary_df['Total Rides'].map('{:,}'.format)
pyber_summary_df['Total Drivers'] = pyber_summary_df['Total Drivers'].map('{:,}'.format)
pyber_summary_df['Total Fares'] = pyber_summary_df['Total Fares'].map('${:,.2f}'.format)
pyber_summary_df['Avg. Fare per Ride'] = pyber_summary_df['Avg. Fare per Ride'].map('${:.2f}'.format)
pyber_summary_df['Avg. Fare per Driver'] = pyber_summary_df['Avg. Fare per Driver'].map('${:.2f}'.format)

pyber_summary_df

"""## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city."""

# 1. Read the merged DataFrame
pyber_data_df.head()

# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.
pyber_grouped_df = pyber_data_df.groupby(['type', 'date']).sum()[['fare']]
pyber_grouped_df

# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
# df = df.reset_index()
pyber_grouped_df = pyber_grouped_df.reset_index()
pyber_grouped_df.head()

# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 
pyber_grouped_df = pyber_grouped_df.pivot(index = 'date', columns = 'type', values = 'fare')
print(pyber_grouped_df.head())

# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.

pyber_grouped_spring = pyber_grouped_df.loc[:'2019-04-29']
pyber_grouped_spring

# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)
pyber_grouped_spring.index = pd.to_datetime(pyber_grouped_spring.index)
pyber_grouped_spring.head()

# 7. Check that the datatype for the index is datetime using df.info()
pyber_grouped_spring.info()

# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
pyber_grouped_week = pyber_grouped_spring.resample('W').sum()
pyber_grouped_week.head()

# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 

pyber_grouped_week.plot(figsize=(18,6), title='Total Fare by City Type')
# plt.title('Total Fare by City Type')
plt.ylabel('Fare ($USD)')
plt.xlabel('')


# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')
plt.savefig('/content/drive/My Drive/Colab Notebooks/PyBer_Analysis/Analysis/challenge.png')
plt.show()

