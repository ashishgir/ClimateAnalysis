#!/usr/bin/env python
# coding: utf-8

# ## Global warming is a hot topic these days. Debate over global warming has been going all around the world.  Temperature visualization is one of the most important arguments in conversations so it's time to plot some data

# In[1]:
import numpy as np
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
class Main():
    def globalTemp(self):
        globaltemp = pd.read_csv('GlobalTemperatures.csv', parse_dates=['dt'])
        #Let's look how average temperature changes over the years:
        year_temp = globaltemp.groupby(globaltemp.dt.dt.year).mean()
        city_rows = year_temp.index
        city_rows = list(city_rows)
        temp={}
        for i in city_rows:
            row = year_temp.loc[i]
            temp[i] = row['LandAverageTemperature']
        return temp

    def globalTempByCity(self, country,city):
        countryCity=city +' ' +country
        bycities = pd.read_csv('combined.csv', parse_dates=['dt'])
        #there are some cities with the same name but in different countries
        bycities[['City', 'Country']].drop_duplicates()
        bycities.City = bycities.City.str.cat(bycities.Country, sep=' ')
        bycities = bycities[bycities.dt.dt.year >= 1900]
        # convert to a city-year table calculating mean year temperature:
        city_means = bycities.groupby(['City', bycities.dt.dt.year])['AverageTemperature'].mean().unstack()
        #city_mins = bycities.groupby(['City', bycities.dt.dt.year])['AverageTemperature'].min().unstack()
        #city_maxs = bycities.groupby(['City', bycities.dt.dt.year])['AverageTemperature'].max().unstack()
        #print("When enter country and city")
        #print(city_means.head())
        first_years_mean = city_means.iloc[:, :5].mean(axis=1) # mean temperature for the first 5 years
        #print(first_years_mean)
        city_means_shifted = city_means.subtract(first_years_mean, axis=0)
        #print("Print shifted data")
        #print(city_means_shifted)
        # select cities from shifteddata
        #print(len(city_means_shifted))
        city_rows = city_means_shifted.index
        row =''
        for c in city_rows:
            if(c.lower()==countryCity.lower()):
                row=city_means.loc[c]
                return row
