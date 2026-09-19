
import pandas as pd

employees = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ravi", "Priya", "Arun"],
   "department": [101, 102, 105]
})

departments = pd.DataFrame({
    "Department_ID": [101, 102],
    "Department": ["IT", "HR"]
})




s=pd.merge(employees,
           departments,
           left_on ="department",
           right_on ="Department_ID",
           how="left"
)
print(s)
