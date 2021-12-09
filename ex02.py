import pandas as pd
dic = {"A":[130,1900,16.3],"B":[250,2600,10.2],"C":[190,2200,11.1],"D":[300,2900,7.1],"E":[210,2400,12.1]}
df = pd.DataFrame(dic,columns=["A","B","C","D","E"])
print(df)