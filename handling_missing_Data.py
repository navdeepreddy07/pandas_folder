import pandas as pd

df=pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\missing_data.csv")
#print(f"Toatl missing values :{df.isnull().sum().sum()} ")
#print(f"tatal percenatge missing vales : {(df.isnull().sum()//len(df))*100}")
#print(df.dropna())
#print(df)
print(df.dropna(subset=["City"]))
