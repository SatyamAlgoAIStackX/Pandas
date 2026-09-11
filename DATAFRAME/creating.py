import numpy as np
import pandas as pd
# Here we are creating DataFrame from Series
s = pd.Series([i for i in "abcdef"])
df = pd.DataFrame(s)
print(df)

# Here we are creating dataFrame from Python List
l = [
    [80,90,110],
    [85,75,65,],
    [7,8,20]
]
df1 = pd.DataFrame(l,columns=("IQ","Percentile","Package"))
print(df1)

# Now we are creating dataFrame from dictionary

Dicts= [
    {"Name":"Satyam Yadav","Roll":1,"Sem": 3},
    {"Name":"Raushan Yadav","Roll":2,"Sem": 3},
    {"Name":"Harshdeep Jha","Roll":3,"Sem": 3}
    
]
df2 = pd.DataFrame(Dicts)
print(df2)