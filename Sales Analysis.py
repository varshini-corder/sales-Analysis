import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#file reading
df = pd.read_csv("sales_dummy_50.csv")
print(df.head())

#to check data set
print(df.info())
print(df.shape)

#Data cleaning
print(df.isnull().sum())

#create sales:
df["sales"] = df["Quantity"] * df["Price"]
print(df.head())

total_s = df["sales"].sum()
print("Total sales =", total_s)


#chart
product_sales = df.groupby("Product")["sales"].sum()

print(product_sales)


product_sales.plot(kind="bar")

plt.title("product sales")
plt.xlabel("product")
plt.ylabel("sales")
plt.show()




