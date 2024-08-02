#starting with pandas::::::::::::::::::::::::::::::series
'''
import pandas as pd
s1=()
s=pd.Series(s1,dtype='int64')
print(s)
print(s.empty)





#write a program to convert a list into series:
import pandas as pd
 
fruits=["mango","apple","banana","cherry","grapes"]
fs=pd.Series(fruits)
#print(fs)
#print(fs.index)
#print(fs.values)
#print(fs.dtype)
#print(fs.shape)
#print(fs.nbytes)
#print(fs.ndim)
#print(fs.size)

#print(fs.itemsize)

print(fs.hasnans)

#print(fs.empty)
 




#write a program to convert dictionary into series:
import pandas as pd
d={1:"khushi",2:"loves",3:"food"}
sd=pd.Series(d)
print(sd)



#write a program to convert a tuple into series:
import pandas as pd
l=(10,20,30,40)
s=pd.Series(l)
print(s)



#write a program to adjust the indexing as per you:
import pandas as pd
l=[2,4,6,8,10]
s=pd.Series(l,["1st","2nd","3rd","4th","5th"])
#print(s["2nd"])
                      ######or######
l=[2,4,6,8,10]
s=pd.Series(l,index=["1st","2nd","3rd","4th","5th"])
print(s)
print(s.index)

             
#write a program using head() and tail():
import pandas as pd
t=[1,2,3,4,5,6,7,8,9,10,11,12]
s=pd.Series(t,index=['a','b','c','d','e','f','g','h','i','j','k','l'])
print(s)
#print(s.head())
#print(s.tail())
print(s.head(2))
print(s.tail(3))



#write a program using selection loc()
import pandas as pd
l=([11,22,33,44,55,66])
s=pd.Series(l)
print(s)
print(s.loc[:2])
print(s.loc[3:4])

#write a program using selection iloc()
import pandas as pd
l=([11,22,33,44,55,66])
s=pd.Series(l)
print(s)
print(s.iloc[:2])
print(s.iloc[3:4])

#write a program using selection[]
import pandas as pd
l=([11,22,33,44,55,66])
s=pd.Series(l)
print(s)
print(s[1])
print(s[3:4])

import pandas as pd 
s1=pd.Series(55,index=[1,8])
 
print(s1.itemsize)


import pandas as pd
fruits=["mango","apple","banana","cherry","grapes"]
fs=pd.Series(fruits)
print(fs)
print(fs.drop(2))
 
    

s=(11,12,13,14)
ser1=pd.Series(s)
print(ser1)

s1=[21,22,23,24]
ser2=pd.Series(s1)
print(ser2)

s3={101:21,102:22,103:23,104:24}
ser3=pd.Series(s3)
print(ser3)


ser4=pd.Series(10,index=[10,102,103,4])
print(ser4)

print(ser3-ser4)
'''
import pandas as pd1
import numpy as np1
data = {'p': 0.,"r": 1.,'e': 2.,'m': 2.}
s=pd1.Series(data,index=['b','c','d','a'])
print(s)






















