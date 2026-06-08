import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


df= pd.read_csv("blinkit_data.csv")
print("Printing blinkit dataset :\n:",df)

#Knowing about dataset
print("top ten rows \n",df.head(10))
print("buttom ten rows \n",df.tail(10))
print("shape of dataset :\n",df.shape)
print("columns in dataset :\n",df.columns)
print("Dtatypes of columns :\n",df.dtypes)
print("info about dataset :\n",df.info())

#Data updatting in particular column(data cleaning)
print("before updating the data :\n",df["Item Fat Content"].unique())
df["Item Fat Content"]=df["Item Fat Content"].replace({'reg':'Regular','low fat':'Low Fat','LF':'Low Fat'})
print('after updating the data ',df["Item Fat Content"].unique())


# Business Requirements 

#total Sales
total_sales = df["Sales"].sum()

#avg sales 
avg_sales =df["Sales"].mean()

#no. of items sold
no_of_items_sold =df["Sales"].count()

#avg ratings 
avg_ratings = df['Rating'].mean()

#Displays the outputs 
print(f"Total sales: ${total_sales:,.1f}")
print(f"Average sales: ${avg_sales:,.1f}")
print(f"No. Of Items Solds: {no_of_items_sold:,.1f}")
print(f"Average Ratings: {avg_ratings:,.1f}")


#Charts Requirements

#total sales by Fat Content
sales_by_fat=df.groupby("Item Fat Content")["Sales"].sum()

plt.pie(sales_by_fat,labels=sales_by_fat.index,autopct="%.1f%%",startangle=90)
plt.title("sales by fat contents")
plt.axis('equal')
plt.show()

#Total sales by items type

sales_by_type =df.groupby("Item Type")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
bars=plt.bar(sales_by_type.index,sales_by_type.values)
plt.xticks(rotation=-90)
plt.xlabel("Items Type")
plt.ylabel("Total Sales")
plt.title("Total Sales by Items Type")

#Accurate sales of each bar in bars 
ax = plt.gca()
ax.bar_label(bars, fmt='{:,.0f}', fontsize=8)
plt.tight_layout()
plt.show()


# Fat Content by Outlets for total sales 
grouped=df.groupby(['Outlet Location Type','Item Fat Content'])['Sales'].sum().unstack()
grouped=grouped[['Regular','Low Fat']]

ax=grouped.plot(kind='bar',figsize=(8,5),title='Outlet tier by item fat content')
plt.xlabel('Outlet location tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')

plt.tight_layout()
plt.show()

#Total sales by outlet establishment year
sales_by_year=df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index,sales_by_year.values,marker='o',linestyle='-')

plt.xlabel('Year Of Establishment')
plt.ylabel('Total Sales')
plt.title("Total sales by outlet establishment year")

for x,y in zip(sales_by_year.index,sales_by_year.values):

    plt.text(x, y, f'{y:,.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()


# Sales by outlet size
sales_by_size=df.groupby('Outlet Size')['Sales'].sum()

plt.figure(figsize=(4,4))
plt.pie(sales_by_size,labels=sales_by_size.index,autopct='%.1f%%',startangle=90)
plt.title("Sales by outlet size")
plt.tight_layout()
plt.show()