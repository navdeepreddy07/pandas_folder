import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [30000, 25000, 45000, 35000, 40000],
    "City": [" Hyderabad ", "Chennai", "Hyderabad", " Mumbai ", "Chennai"]
})

# Find all IT employees whose salary is greater than 35000, and display only:


df["City"]=df["City"].str.strip()
df[]