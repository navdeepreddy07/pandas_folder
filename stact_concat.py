import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Ravi", "Priya"],
    "Age": [21, 19]
})

df2 = pd.DataFrame({
    "Name": ["Arun", "Sneha"],
    "Age": [23, 20]
})

print(pd.concat([df1,df2],axis=1))