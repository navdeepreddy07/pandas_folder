# "C:\Users\Navadeep Reddy\Downloads\matches_Datasets.csv"

import pandas as pd #importing datasets..
import numpy as np 



df=pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\matches_Datasets.csv") # loaded dataset..
print(df.shape)  # reurns no of rows , columns 
print(df.index) # return no of rown in dataset
print(df.columns)

print(df.info()) # knonw about the dataset

# find null values

print(df.isnull().sum()) # finding null values for each column
print(df.isnull().sum().sum()) # finding total no of null values in dataset

# filling data with most repeated city or we use simply "UN known"
df["city"]=df["city"].fillna(df["city"].mode()[0])
print(df.isnull().sum())
print("\n")

# filling data in player of the match ex: unknown
print("\n")
df["player_of_match"]=df["player_of_match"].fillna("NO award")
print(df.isnull().sum())


# filling data in winner coloum ex: no winner

df["winner"]=df["winner"].fillna("No winner")
print(df.isnull().sum())


# cleaning coloums and  store only requried columns

df=df.drop(columns=["umpire1","umpire2"],errors="corese")
print(df.isnull().sum())
print(df.head())

# analysing data
  
# finding no of matches per season

print(df["season"].value_counts().sort_index())

# finding most winning teams 

print(df["winner"].value_counts())


# how many matches ended with no result

s=df[df["winner"]=="No winner"]
print(f"\nHaving No Result IN matches is :{len(s)}")
 # all data who has no result


#most player of the match of all seasons

s=df["player_of_match"].value_counts().sort_values(ascending=False)
print(s.head(1))     

#common toss decisions 
print(df["toss_decision"].value_counts())

#matches ended wth smallest and largest margines

result=df[df["result"]=="runs"].sort_values(by="result_margin",ascending=False).head(1)
print(result)

print(df.isnull().sum())


#lowest score and win
result=df[df["result"]=="wickets"].sort_values(by="result_margin",ascending=True).head(1) 
print(result)

#how many were decided by dl method

r=df["method"].notnull().sum()
print(r)


#which team wons most fnals

print(df.columns)

f=df[df["match_type"]=="Final"]["winner"].value_counts()
print(f)