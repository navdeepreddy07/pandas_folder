import pandas as pd

df=pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\Amazon Sale Report.csv_Datasets.zip")

# print(df.info())

# print(df.head())

print(df.columns)

# #finding missing values in data and sort from (high to low)

# missing=df.isnull().sum()

# print(missing.sort_values(ascending=False))

# s=df["fulfilled-by"].value_counts()

# #percentage of missing percentage on filfilled-by

# missing=(89698 / 128975 * 100)

# print(missing) #  69.54681139755766

# #same missing-percentage analysis for Amount

# missing_amount=(7795 / 128975*100)

# print(missing_amount) # 6.04 %

# #missig percenatge for promotion-ids

# missing_promotion = ( 49153 / 128975)*100

# print(missing_promotion) # 38.110486528396976

# #percentage for Unnamed: 22.

# missing_unamed=(49050/128975)*100

# print(missing_unamed) # 38.03062609032759

# # # # find out values in unamed:22

# s=df["Unnamed: 22"].value_counts()

# print(s)

# analysis=df["Amount"].nunique()

# print(analysis)

# #“What is the highest single order amount in each category?”

# high=df.groupby("Category")["Amount"].sum()

# print(high.sort_values(ascending=False))

# # # # Which category has the highest number of items/orders sold

# print(df.info())

# total=df.groupby("Category")["Qty"].sum()

# print(total.sort_values(ascending=False))

# #Which category has the highest average order value?

# total=df.groupby("Category")["Amount"].mean()

# print(total.sort_values(ascending=False))


# #Which states generate the highest total sales amount?
# #This gives us total sales amount for every state, sorted from highest to lowest.
# total=df.groupby("ship-state")["Amount"].sum()
# print(total.sort_values(ascending=False))

# #Which states have the highest total number of items sold?

# total=df.groupby("ship-state")["Qty"].sum()

# print(total.sort_values(ascending=False))

# #Which SKUs generated the highest total sales amount?
# total=df.groupby("SKU")["Amount"].sum()
# print(total.sort_values(ascending=False))

# print(df["Status"].value_counts().sort_values(ascending=False))


# # # Which sales channel appears in the dataset, and how many orders came through each channel


#  #cleaning columns names 
df.columns=df.columns.str.strip().str.replace(" ","_").str.replace("-","_").str.title()
print(df.columns)

# print(df["Sales_Channel"].value_counts())


# df["Date"]=pd.to_datetime(df["Date"])
# print(df["Date"])


# #k: Check the datatype of Date after conversion.

# print(df["Date"].dtype)


# # # Keep only Amazon-fulfilled orders
# df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
# amazon_by=df[df["Fulfilment"]== "Amazon"]
# monthly_sales = amazon_by.groupby(
#      amazon_by["Date"].dt.month
# )["Amount"].sum()

# new=monthly_sales.iloc[0]
# print(new)

# #How many Amazon-fulfilled orders/rows belong to March?

# #What percentage of orders were cancelled?

# print(df.columns)

# new=df[df["Status"]=="Cancelled"]
# total=new["Status"].value_counts()
# per=(total / 128975) *100
# print(per)


# # What percentage of orders were fulfilled by Amazon vs Merchant?

r=df["Fulfilment"].value_counts()
print((r.iloc[0]/len(df))*100)
print((r.iloc[1]/len(df))*100)


#cal order vs un order in status coloum
t=df[df["Status"]=="Cancelled"]
print(len(t)/len(df)*100)