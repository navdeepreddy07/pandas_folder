import pandas as pd




df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran", "Anu", "Rahul"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "Sales", "HR"],
    "City": ["Hyderabad", "Chennai", "Hyderabad", "Mumbai", "Chennai", "Hyderabad", "Chennai"]
})
# Now find the percentage of employees in each city.

s=df["Department"].value_counts()  # we also use normal normalize=true but i gives the decimal values when we use 100 it gives the percentage values

print(s.sort_values(ascending=True))