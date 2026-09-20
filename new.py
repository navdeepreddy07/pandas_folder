import pandas as pd

data={"Name":["vamsi","Durga","deepu"],
      "subject":["maths","science","physics"],
      "marks":[90,85,95],
      "passsed":["True","False","NAN"]
      }

table=pd.DataFrame(data)
#print(table.info())
#print(table.memory_usage())
#print(table.select_dtypes(exclude="int"))

#print(table[["Name","subject"]])


    
print(table[(table["marks"]) > 90 ])
print(table.dropna())