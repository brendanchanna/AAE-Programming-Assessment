#!/usr/bin/env python
# coding: utf-8

# In[558]:


import pandas as pd
import numpy as np
print('Hello: To begin using this program, enter the directory path for the csv file you would like to analyze. \nThe path can be entered into the variable df in the code above.')
#import dataset into dataframe
df = pd.read_csv(r'Example.csv')
print('\n')
#Return total number of fruit
fruit = df['fruit']
total_fruit = len(fruit)
if total_fruit > 1:
    print('There are ' + str(total_fruit) + ' fruits.')
elif total_fruit == 1:
    print('There is '+ str(total_fruit)+ ' fruit')
else:
    print('There are either zero fruits in the file or the file is incorrectly formatted.')
print('\n') 



#Return types of fruit
types_fruit = len(fruit.unique())
if types_fruit > 1:
    print('There are ' + str(types_fruit) + ' types of fruit.')
elif types_fruit == 1:
    print('There is ' + str(types_fruit) + ' type of fruit.')
else:
    print('There are either zero fruits in the file or the file is incorrectly formatted.')
print('\n') 




#Return number of each fruit
count_types = df.groupby('fruit')['fruit'].count().sort_values(ascending=False)
for i in range(len(count_types)):
    print('There are ' + str(count_types[i]) + ' ' + str(count_types.index[i]) + 's')
print('\n')


#Return characteristics of fruit 
df4 = df.groupby('fruit').agg(list)
df4 = df4.drop(columns = 'days')
df4['Combined_char'] = [df4['characteristic1'][i] + df4['characteristic2'][i] for i in range(len(df4))]
df4_display = df4['Combined_char'].map(pd.unique)
print('The characteristics of each fruit are displayed below: ')
print(df4_display)
 
        
print('\n')
#Count the number of old fruit
from collections import Counter
#Generate list for old fruit
old_fruits = []
#iterate through the df to find and append fruit to the list
for i in range(len(df['fruit'])):
    if df['days'][i] >= 3:
        old_fruits.append((df['fruit'][i]))
#Use Counter to calculate and pair fruit frequencies
OF = Counter(old_fruits)
for key, value in OF.items():
    if value > 1:
        print('There are '+ str(value) + " " + str(key)+'s that are over 3 days old.')
    if value == 1:
        print('There is ' + str(value) + " " + str(key) + ' that is over 3 days old.')


# In[ ]:




