import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female"],
    "Salary": [30000, 40000, 25000, 35000, 28000, 32000]
})

# Create a pivot table showing the maximum salary for each Department and Gender.

s=pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="max"



)
print(s)