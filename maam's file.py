# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#import pandas as pd
#s = pd.Series([10,20,30,40,50,60,72,74],index=['a','b','c','d','e','f','g','h'])
#s1=pd.Series([8,7,6,5,4,3,2,1], index=['a',â€™bâ€™,â€™câ€™,â€™dâ€™,â€™eâ€™,â€™fâ€™,â€™g,â€™hâ€™])


# Write a program a list into series.


import pandas as pd
l = [10,20,30,40]   #List
s = pd.Series(l)
print(s)
print(l)


d = {"A":"Apple",2:"Orange",3:"Papaya"}    # Dictionary
s = pd.Series(d)
print(s)


l = (10,20,30,40,50,60,70,80,90,100,22,33,545,66,77,44)    # Tuple
s = pd.Series(l)
print(s.head(2))
print(s.tail())


#l = [10,20,30,40]
#s = pd.Series(l,index=[100,200,300,400])    # index explicitly
#print(s)


l = (10,20,30)    # Tuple
s = pd.Series(l,index=(100,200,300))
#s = pd.Series(l)
print(s)
print(s.iloc[7:11])
print(s[3:6])


l = [10,20,30,40]   #List
s = pd.Series([34,54,66])
df = pd.DataFrame(s)
print(df)


dic = {'A':[1,2,3],'B':[200,300,400]}
df = pd.DataFrame(dic)
print(df)


empdata={'empid':[101,102,103,104,105,106],
'ename':['Sachin','Vinod','Lakhbir','Anil','Devinder','UmaSelvi'],'Doj':['12-01-2012','15-01-2012','05-09-2007','17-01- 2012','05-09-2007','16-01-2012'] }
df=pd.DataFrame(empdata)
print(df)
#print(df[["Doj","empid","ename"]])
print(df[["empid","Doj"]])
print(df.empid)


s = pd.Series([1,2,3,4,5])
df = pd.DataFrame(s)
df.columns = ['List1']
df['List2'] = 20
print(df)

df['List3']= df['List1'] + df['List2']
print(df)
print(df.List2)
print(df[['List2','List1']])


s= pd.Series([10,20,30,40])
df=pd.DataFrame(s)
df.columns=["List1"]
df["List2"]=50
df1=df.drop("List2",axis=1) #(axis=1) means to delete Data column wise

df2=df.drop(df.index[[0,2]],axis=0) #(axis=0) means to delete data row wise with given index
print(df)
print("After deletion::")
print(df1)
print ("After row deletion::")
print(df2)


#Note : if you are not mentioning the axis by default it is 0 i.e. row

s= pd.Series([10,20,30,40])
df=pd.DataFrame(s)
df.columns=["List1"]
df["List2"]=50
print(df)
df1 = df.drop(df.index[[0,1]],axis=0,inplace = False) #inplace = true that means it will delete the data permanentaly from the memory or it will make changes in the original data.
# inplace = false - it will return the new dataframe with deleted values. Original dataframe remains the same.
print(df1)