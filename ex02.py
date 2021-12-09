import pandas as pd
dic = {"마력":[130,250,190,300,210],"총중량":[1900,2600,2200,2900,2400],"연비":[16.3,10.2,11.1,7.1,12.1]}
df = pd.DataFrame(dic,columns=["A","B","C","D","E"])
print(df)