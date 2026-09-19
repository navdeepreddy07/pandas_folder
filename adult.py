import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha"],
    "Age": [21, 19, 23, 20],
    "Salary": [30000, 25000, 45000, 35000]
})


#df["Salary_Level"] = df["Salary"].apply(lambda salary : "hiGH" if salary >= 40000 else "low")
#print(df)
print(df.sort_values(by=["Salary","Age"],ascending=[False,True]))
