#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_excel("C:/Users/2024/Downloads/Retail_Sales_Task_Dataset.xlsx")


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


#Data Cleaning missing values
df.isnull().sum()


# In[10]:


df.duplicated().sum()


# In[12]:


df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['ShipDate'] = pd.to_datetime(df['ShipDate'])


# In[14]:


df.dtypes


# In[15]:


df['ShippingDays'] = (df['ShipDate'] - df['OrderDate']).dt.days


# In[17]:


df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month
df['MonthName'] = df['OrderDate'].dt.month_name()


# In[18]:


df['ProfitMargin'] = (df['Profit'] / df['Sales']) * 100


# In[19]:


total_sales = df['Sales'].sum()
total_sales


# In[20]:


total_profit = df['Profit'].sum()
total_profit


# In[21]:


total_cost = df['Cost'].sum()
total_cost


# In[22]:


total_orders = df['OrderID'].nunique()
total_orders


# In[23]:


average_order_value = df['Sales'].mean()
average_order_value


# In[24]:


category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

category_sales


# In[25]:


category_sales.plot(kind='bar', figsize=(8,5))

plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.show()


# In[26]:


category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

category_profit.plot(kind='bar', figsize=(8,5))

plt.title('Profit by Category')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.xticks(rotation=0)
plt.show()


# In[27]:


top_products = (
    df.groupby('Product')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products


# In[28]:


bottom_products = (
    df.groupby('Product')['Sales']
    .sum()
    .sort_values()
    .head(10)
)

bottom_products


# In[29]:


region_sales = (
    df.groupby('Region')['Sales']
    .sum()
    .sort_values(ascending=False)
)

region_sales


# In[30]:


region_sales.plot(kind='bar', figsize=(8,5))

plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()


# In[31]:


top_customers = (
    df.groupby(['CustomerID', 'CustomerName'])['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_customers


# In[32]:


salesperson_performance = (
    df.groupby('Salesperson')
    .agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'OrderID': 'nunique'
    })
    .sort_values('Sales', ascending=False)
)

salesperson_performance


# In[33]:


payment_sales = df.groupby('PaymentMethod')['Sales'].sum()

payment_sales.plot(
    kind='pie',
    autopct='%1.1f%%',
    figsize=(7,7)
)

plt.title('Sales by Payment Method')
plt.ylabel('')
plt.show()


# In[34]:


monthly_sales = (
    df.groupby('Month')['Sales']
    .sum()
)

monthly_sales.plot(
    kind='line',
    marker='o',
    figsize=(10,5)
)

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid()
plt.show()


# In[35]:


df[['Discount', 'Sales', 'Profit']].corr()


# In[36]:


sns.scatterplot(
    data=df,
    x='Discount',
    y='Profit'
)

plt.title('Discount vs Profit')
plt.show()


# In[37]:


df['ShippingDays'].describe()


# In[40]:





# In[ ]:




