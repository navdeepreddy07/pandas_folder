import pandas as pd

df=pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\StoreData (1).csv")

print(df)
df.columns=df.columns.str.strip().str.title().str.replace(" ","_")
#print(df.drop_duplicates())

df["Salas"]=pd.to_numeric(df["Sales"],errors="Coerce")
print(df["Sales"])