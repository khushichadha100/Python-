#starting with pandas::::::::::::::::::::::::::::::series

#write a program to convert a list into series:
import pandas as pd
fruits=["mango","apple","banana","cherry"]
fs=pd.Series(fruits)
print(fs)



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
l=[2,4,6,8,10]
s=pd.Series(l,["1st","2nd","3rd","4th","5th"])
print(s)
                      ######or######
l=[2,4,6,8,10]
s=pd.Series(l,index=["1st","2nd","3rd","4th","5th"])
print(s)


                     
#write a program using head() and tail():
import pandas as pd
t=(1,2,3,4,5,6,7,8,9,10)
s=pd.Series(t)
print(s)
print(s.head())
print(s.tail())
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


    









