import pandas as pd 

# df = pd.DataFrame({
#     "Name": ["Ravi", "Priya", "Arun", "Sneha"],
#     "Department": ["IT", "HR", "IT", "HR"],
#     "Salary": [30000, 25000, 45000, 35000]
# })

#  #Find the average salary for each department.


# s=df.groupby("Department")["Salary"].mean()
# # print(s)

# employees = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Name": ["Ravi", "Priya", "Arun"],
#     "Dept_ID": [101, 102, 103]
# })

# departments = pd.DataFrame({
#     "Dept_ID": [101, 102],
#     "Department": ["IT", "HR"]
# })


# #  Merge them so that all employees are retained, even if their department doesn't exist in departments.
 
# s=pd.merge(employees,
#            departments,
#            on="Dept_ID",
#         #    how="outer"
# )
# print(s)



# df1 = pd.DataFrame({
#     "Name": ["Ravi", "Priya"],
#     "Age": [21, 19]
# })

# df2 = pd.DataFrame({
#     "Name": ["Arun", "Sneha"],
#     "Age": [23, 20]
# })


# s=pd.concat([df1,df2],ignore_index=True)
# print(s)


df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran", "Anu"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "Sales"],
    "Salary": [30000, 25000, 45000, 35000, 40000, 28000],
    "Age": [21, 19, 23, 20, 25, 22]
})

# Task:

# Find the average salary of employees in each department, then sort the result from highest average salary to lowest.

# Don't worry if you need to

s=df.groupby("Department")["Salary"].mean()
print(s.sort_values(ascending=False))
