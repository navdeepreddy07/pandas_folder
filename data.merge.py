
    "Salary": [30000, 25000, 45000]
})

performance = pd.DataFrame({
    "ID": [1, 2, 3],
    "Salary": [32000, 27000, 48000],
    "Rating": [4, 5, 4]
})

s=pd.merge(employees,
           performance,
           on="ID",
           suffixes=("_employee","_performance") #(left_salary,right_salary)
)
print(s)