import pandas as pd

df=pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\House_Rent_Dataset.csv")
#print( df[df["Rent"] < 10000])
#semi=df[df["Furnishing Status"]=="Semi-Furnished"]
#print(semi)
#bathroom=df[df["Bathroom"] > 1]
#print(bathroom)

print(df[df["Rent"] > 15000])
print(df.reset_index())