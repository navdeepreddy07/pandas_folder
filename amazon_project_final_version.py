import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\Amazon Sale Report.csv_Datasets.zip")

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.title()
)

# Convert Date to Pandas datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove unwanted column
df = df.drop(columns=["Unnamed:_22"])


# =========================
# Data Analysis
# =========================

# Which product category generated the highest total sales?
s = df.groupby("Category")["Amount"].sum()
print(s.sort_values(ascending=False))


# Which product categories sold the highest number of items?
y = df.groupby("Category")["Qty"].sum()
print(y.sort_values(ascending=False))


# Which states generated the highest total sales?
p = df.groupby("Ship_State")["Amount"].sum()
print(p.sort_values(ascending=False))


# Which states sold the highest number of items?
p = df.groupby("Ship_State")["Qty"].sum()
print(p.sort_values(ascending=False))


# Which SKUs sold the highest number of items?
print(df.groupby("Sku")["Qty"].sum().sort_values(ascending=False))


# Which SKUs generated the highest total sales?
print(df.groupby("Sku")["Amount"].sum().sort_values(ascending=False))


# What is the distribution of orders by status?
print(df["Status"].value_counts())


# How many orders were fulfilled by Amazon vs Merchant?
print(df["Fulfilment"].value_counts())


# Which month generated the highest total sales?
r = df.groupby(df["Date"].dt.month)["Amount"].sum()
print(r.sort_values(ascending=False))


# What percentage of orders were cancelled?
l = df[df["Status"] == "Cancelled"]
print((len(l) / len(df)) * 100)


# =========================
# Business Insights
# =========================

# Amazon fulfilment handled approximately 69.55% of the recorded orders.

# Approximately 14% of recorded orders were cancelled.

# April recorded the highest total sales among the analyzed months.

# Maharashtra recorded the highest quantity of products sold among the analyzed states.

# Sales and quantity varied across SKUs, with some products contributing
# significantly more than others.
