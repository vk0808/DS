#!/usr/bin/env python
# coding: utf-8

# In[24]:

# Importing Modules
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Read the data and print first few rows
d = pd.read_csv('gapminder-FiveYearData.csv')
df = pd.DataFrame(d)
print("Dataframe")
print(df.head())

#Create a pivot_table for making heatmaps
table = pd.pivot_table(df, values='lifeExp', index='continent', columns='year', aggfunc=np.sum)
print("Dataframe Pivot Table")
print(table)

#Create heatmap and save the figure to png format
fig = sb.heatmap(table)
plt.savefig('Seaborn.png')

