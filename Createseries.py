import pandas as pd
import numpy as np
# Create series from ndarray 
arr = np.array(np.arange(1,11))
s = pd.Series(arr)
print(s)

# Create series from ndarray with labeing
s1 = pd.Series(arr,index=[x for x in "abcdefghij"])
print(s1)

# Create series from python list
l = [x for x in range(1,11)]
s2 = pd.Series(l,index=[i for i in "abcdefghij"])
print(s2)

# Create series from dictionary
d = {
    "Name" : "Satyam Yadav",
    "Roll No" : 25,
    "Course" : "B-Tech"

}
s3 = pd.Series(d)
print(s3)

# Create series from Scalar value
s4 = pd.Series((50),index=['a','b','c','d','e'])
print(s4)

# Create series by range fuction
s5= pd.Series(range(1,11,2))
print(s5)