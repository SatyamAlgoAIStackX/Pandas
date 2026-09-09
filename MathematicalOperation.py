import numpy as np
import pandas as pd
arr = np.arange(1,5)
s = pd.Series(arr)
# Multipy series with 2 
print(s*2) # output - multiply all original data by two

# Power of all value raise by 2
print(s**2)

# Find value which is greater than 2
print(s[s>2])

print("---additional operation---")
s1 = pd.Series(range(1,6),index=[x for x in "abcde"])
s2 = pd.Series(range(6,11),index=[x for x in "abcde"])
s3 = pd.Series(range(11,15),index=[x for x in "abcd"])
# Normal addition one to one
print(s1+s2)
# Here we are adding non matching index series so where sereis has output NaN value
print(s2+s3)
# Here We are adding non matching series but we filled that index with 0 then expected output is printed
print(s2.add(s3,fill_value=0))