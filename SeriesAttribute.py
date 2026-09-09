import numpy as np
import pandas as pd
l=[i for i in range(1,11)]
s = pd.Series(l,index=[x for x in "abcdefghij"])
#1 head() used to find first 5 data and head(k) find first k item in Series
print(s.head())
print(s.head(3))

#2 tail() used to find last five items and tail(k) find last k items in Series
print(s.tail())
print(s.tail(3))
#3 count() ---No. of items in series
print(s.count())
#4 .values --- give values of series
print(s.values)
#5 .keys --- give index of series
print(s.keys)
#6 .hasnans -- give nan value if preint or not
print(s.hasnans)

#8 .dtypes ---retuen data types
print(s.dtypes)



