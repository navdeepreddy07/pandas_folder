import pandas as pd

df=pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\Amazon Sale Report.csv_Datasets.zip")

# print(df.info())
# print(df.head())

print(df.columns)

#cleaning coloum names

df.columns=df.columns.str.strip().str.replace(" ","_").str.replace("-","_").str.title()
print(df.columns)

#Convert Date from its original format into Pandas datetime format
df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
print(df["Date"].head(3))

# Data processing 

# we are removing unwanted coloum Unnamed:_22'
df=df.drop(columns=["Unnamed:_22"])
print(df.columns)

#Analysing

# Which product category generated the highest total sales?
s=df.groupby("Category")["Amount"].sum()
print(s.sort_values(ascending=False))

# Which product categories sold the highest number of items?
y=df.groupby("Category")["Qty"].sum()
print(y.sort_values(ascending=False))

# Which states generated the highest total sales

p=df.groupby("Ship_State")["Amount"].sum()
print(p.sort_values(ascending=False))

# Which states sold the highest number of items?


p=df.groupby("Ship_State")["Qty"].sum()
print(p.sort_values(ascending=False))



# Which SKUs sold the highest number of items?

print(df.groupby("Sku")["Qty"].sum().sort_values(ascending=False))

#: Which SKUs generated the highest total sales?

print(df.groupby("Sku")["Amount"].sum().sort_values(ascending=False))

# What is the distribution of orders by status
print(df["Status"].value_counts())

# How many orders were fulfilled by Amazon vs Merchant?
print(df["Fulfilment"].value_counts())

# Which month generated the highest total sales?
r=df.groupby(df["Date"].dt.month)["Amount"].sum()
print(r.sort_values(ascending=False))

# What percentage of orders were cancelled?

l=df[df["Status"]=="Cancelled"]
print((len(l)/len(df))*100)

# =========================
# Business Insights
# =========================

# April recorded the highest Amazon-fulfilled sales among the analyzed months.

#Insight 4 — State Performance

# Maharashtra recorded the highest quantity of products sold among the analyzed states.

# Final Insight — Product Performance
# Sales and quantity varied across SKUs, with some products contributing significantly more than others.