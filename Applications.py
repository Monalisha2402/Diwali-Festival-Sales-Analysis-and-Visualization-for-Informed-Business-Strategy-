# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
from Definations import *
from choice import show_menu
import seaborn as sns


# import csv file
df = pd.read_csv('Diwali_Sales.csv', encoding= 'unicode_escape')


###Preprocessing

#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# drop null values
df.dropna(inplace=True)

# change data type
df['Amount'] = df['Amount'].astype('int')

#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})

# Exploratory Data Analysis

#Taking choice Input
choice = show_menu()

if choice==1:
    Gender_Insights(df)
elif choice==2:
    Age_Insights(df)
elif choice==3:
    State_Insghts(df)
elif choice==4:
    Marital_Insights(df)
elif choice==5:
    occupation_Insights(df)
elif choice==6:
    Product_Insights(df)
else:
    print("wrong choice")







