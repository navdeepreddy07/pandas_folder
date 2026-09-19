import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha"],
    "Age": [21, 19, 23, 20],
    "Salary": [30000, 25000, 45000, 35000]
})


def check(salary):

    if salary >= 40000 :

        tax = (salary *20 /100)

        total_tax =salary-tax
        return total_tax
    else :

         tax = (salary *10 /100)
         total_tax =salary-tax
         return total_tax


df["After_Tax"] = df["Salary"].apply(check)
print(df)





    


