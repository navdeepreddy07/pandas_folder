import pandas as pd

employees = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ravi", "Priya", "Arun", "sneha"],
    "Dept_ID": [101, 102, 101, 103]
})

departments = pd.DataFrame({
    "Dept_ID": [101, 102, 103],
    "Department": ["IT", "HR", "Sales"]
})

#v=pd.merge(employees, departments, on="Dept_ID", how="left")
#print(v)

s=pd.merge(employees, departments, on="Dept_ID", how="outer")
print(s)