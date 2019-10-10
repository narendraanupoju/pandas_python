# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:59:43 2019

@author: narendra
"""
import pandas as pd
#import pandas_profiling as pdf
import easygui as eg
#choose file from dialog box
directory = eg.fileopenbox()
#directory = '/Example.csv'
data = pd.read_csv(directory, delimiter=';')

#to get the list of coloums names in the dataset
name_of_cols = data.columns.values

#to get total no of coloums 
no_of_cols = data[name_of_cols[0]].size

def percentage(part, whole):
  return 100 * float(part)/float(whole)

#to print the total number of entries each coloumn and %of missing data for each coloumn
for x in name_of_cols:
    print('Total no.of entries in '+x , data[x].dropna().size)
    print('precentage of missing data in '+x ,percentage(data[x].size- data[x].dropna().size, data[x].size))

#to split the data into respective Customer market groups
cust_markt_grups = data['Customer Market Group'].dropna().unique()
print('Total number of customer market group is', cust_markt_grups.size)
print('list of customer market groups', cust_markt_grups)
customers_in_consumer_group = data.loc[data['Customer Market Group']=='Consumer']
customers_in_eng_group= data.loc[data['Customer Market Group']=='Engineering']
customers_in_Tecn_group= data.loc[data['Customer Market Group']=='Technology']
customers_in_Auto_group = data.loc[data['Customer Market Group']=='Automotive']
customers_in_pharma_group = data.loc[data['Customer Market Group']=='Pharma']
customers_in_Chemical_group = data.loc[data['Customer Market Group']=='Chemicals']

#to print the list of customer names in different market groups
print('list of customer names in ')
print('consumer group', customers_in_consumer_group['Customer Name'].unique())
print('engineering group', customers_in_eng_group['Customer Name'].unique())
print('technology group', customers_in_Tecn_group['Customer Name'].unique())
print('automotive group', customers_in_Auto_group['Customer Name'].unique())
print('pharma grouo', customers_in_pharma_group['Customer Name'].unique())
print('chemical group', customers_in_Chemical_group['Customer Name'].unique())

#to get the list of origin airports
print('list of origin airports', data['Origin Airport'].unique())
#to get the list of destination airports
print('list of destination airports', data['Destination Airport'].unique())

#report = pdf.ProfileReport(data)
#report.to_file("report.html")