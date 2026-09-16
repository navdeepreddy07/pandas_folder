
import pandas as pd

df = pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\netflix_titles.csv")
print(df.columns)
df1=df.set_index("show_id")

print(df1.loc["s1","type"])




