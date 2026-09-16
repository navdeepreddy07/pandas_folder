import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Ravi", "Priya", "Arun"],
        "Age": [21, 19, 23],
        "Salary": [30000, 25000, 45000]
    },
    index=["A", "B", "C"]
)

df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha"],
    "Age": [21, 19, 23, 20],
    "Salary": [30000, 25000, 45000, 35000],
    "City": ["Vijayawada", "Hyderabad", "Chennai", "Vijayawada"]
})

df[df["Age"] > 20] 


import pandas as pd

df = pd.read_csv(r"C:\Users\Navadeep Reddy\Downloads\netflix_titles.csv")
print(df.columns)
df1=df.set_index("show_id")

print(df1.loc["s1","type"])




