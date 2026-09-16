import pandas as pd

df=pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\missing_data.csv")
print(df.dropna())