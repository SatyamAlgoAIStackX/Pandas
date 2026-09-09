import numpy as np
import pandas as pd
Dict = {
    "Satyam" : 90,
    "Raushan" : 80,
    "harshdeep": 70,
    "Aman":85,
    "Anshu":75
}
s = pd.Series(Dict)
print(s)
# Here loc method is for accesing value through labeling and ending is included
s1 = s.loc["Satyam":'Anshu']
print(s1)
s2 = pd.Series(np.arange(1,11))
# Here we are  using iloc method for accesing value through index here last element is not included
s3 = s2.iloc[0:5]
print(s3)
# Here we are using normal method to find the element from series
print(s2[5])
print(s2[s2>7])