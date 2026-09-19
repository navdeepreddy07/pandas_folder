import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran", "Anu", "Rahul", "Meena"],
    "Age": [21, 19, 23, 20, 25, 22, 24, 20],
    "Salary": [30000, 25000, 45000, 35000, 40000, 30000, 45000, 35000],
    "City": ["Hyderabad", "Chennai", "Hyderabad", "Mumbai", "Chennai", "Hyderabad", "Mumbai", "Chennai"]
})


print(df.sort_values(by=["City","Salary"],ascending=[True,False]))