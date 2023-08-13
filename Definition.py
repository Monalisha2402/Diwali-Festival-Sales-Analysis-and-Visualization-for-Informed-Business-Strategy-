
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
from choice import show_menu
import seaborn as sns


### Gender based definations

def Gender_Insights(df):
    ax = sns.countplot(x='Gender', data=df)
    for bars in ax.containers:
        ax.bar_label(bars)
    plt.show()
    sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)
    plt.show()

    print("*****From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men****")



### Age based definations

def Age_Insights(df):


    ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

    for bars in ax.containers:
        ax.bar_label(bars)
    plt.show()
    sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)
    plt.show()

    print("*****From above graphs we can see that most of the buyers are of age group between 26-35 yrs female****")




### State based insights

def State_Insghts(df):

    sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data = sales_state, x = 'State',y= 'Orders')
    plt.show()
    sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data = sales_state, x = 'State',y= 'Amount')
    plt.show()
    
    print("*****From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively****")





### Marital Status Based Insights

def Marital_Insights(df):

    ax = sns.countplot(data = df, x = 'Marital_Status')

    sns.set(rc={'figure.figsize':(7,5)})
    for bars in ax.containers:
        ax.bar_label(bars)
    plt.show()

    sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

    sns.set(rc={'figure.figsize':(6,5)})
    sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')
    plt.show()
    
    print("*****From above graphs we can see that most of the buyers are married (women) and they have high purchasing power****")





### Occupation Based


def occupation_Insights(df):

    sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(data = df, x = 'Occupation')

    for bars in ax.containers:
        ax.bar_label(bars)
    plt.show()
    sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')
    plt.show()

    print("*****From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector****")


def Product_Insights(df):

    sns.set(rc={'figure.figsize':(20,5)})
    ax = sns.countplot(data = df, x = 'Product_Category')

    for bars in ax.containers:
        ax.bar_label(bars)
    plt.show()

    sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')
    plt.show()

    print("*****From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category****")


    sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
    sns.set(rc={'figure.figsize':(20,5)})
    sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')
    plt.show()

    fig1, ax1 = plt.subplots(figsize=(12,7))
    df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

