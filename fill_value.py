import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Sales"],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Salary": [30000, 40000, 25000, 35000, 28000]
})

s=pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean",
    fill_value=0

)
print(s)