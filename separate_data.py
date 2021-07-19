import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('file_example_XLSX_100.xlsx')   # an example data that have some information about people in france & united states and great britain
df['Date'] = pd.to_datetime(df['Date'])                   # my data have 100 rows and 8 columns

count_us = 0    # count of people in united stats
count_f = 0     # count of people in france
count_gb = 0     # count of people in great birtain

for i in range(100):
    if df['Country'][i] == 'United States':
        count_us += 1
    
    elif df['Country'][i] == 'France':
        count_f += 1
    
    else:
        count_gb += 1
        
count = []      # count of all people
count.append(count_us)
count.append(count_gb)
count.append(count_f)        

# Let's plot the pie chart for people

x = df['Date'].unique()
y = df['Country'].unique()
plt.pie(count,labels=y)
plt.legend()
plt.show()    # Display the chart

