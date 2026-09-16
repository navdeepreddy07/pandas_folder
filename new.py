import pandas as pd

data={"Name":["vamsi","Durga","deepu"],
      "subject":["maths","science","physics"],
      "marks":[90,85,95],
      "passsed":["True","False","True"]
      }

table=pd.DataFrame(data)
table