# here is .py file of dataanalyst_simple.ipynb

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('file_example_XLSX_100.xlsx')
df['Date'] = pd.to_datetime(df['Date'])
df = df.drop(columns=0)


count_us = 0
count_f = 0
count_gb = 0

for i in range(100):
    if df['Country'][i] == 'United States':
        count_us += 1
    elif df['Country'][i] == 'France':
        count_f += 1
    else:
        count_gb += 1


count = []
count.append(count_us)
count.append(count_gb)
count.append(count_f)


female = df.where(df['Gender']=='Female')
female = female.dropna()

male = df.where(df['Gender']=='Male')
male = df_male.dropna()

male['Date'] = pd.to_datetime(male['Date'])
female['Date'] = pd.to_datetime(female['Date'])

x = df['Date'].unique()
y = df['Country'].unique()
plt.pie(count,labels=y)
plt.legend()
plt.show()

x1 = df.groupby('Date').count()
c3 = []
for i in range(3):
    c3.append(x['Age'][i])  

plt.pie(c3 ,labels=x)
plt.legend()
plt.show()
