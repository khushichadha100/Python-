import pandas as pd
'''
#CREATING EMPTY SERIES:-
s=pd.Series()
print(s)
'''
#CREATING SERIES FROM LIST:-
friends=['vibhu','sandra','disha','nikita']
s1=pd.Series(friends)
print(s1[::-3])
'''           #############OR##############
s1=pd.Series(['vibhu','sandra','disha','nikita'])
print(s1)

#CREATING SERIES FROM 2 LISTS:-
months=['jan','feb','mar','apr']
no_days=[31,28,31,30]
s2=pd.Series(months,index=no_days)
print(s2)

                ########replacing index from values##############
months=['jan','feb','mar','apr']
no_days=[31,28,31,30]
s2=pd.Series(no_days,index=months)
print(s2)

#CREATING SERIES FROM SCALAR OR CONSTANT VALUE:-
s3=pd.Series('khushi',index=['k','h','u','s','h','i'])
print(s3)
                      ########OR########
s3=pd.Series('a very happy birthday !',index=range(1,11,1))
print(s3)

#CREATING SERIES FROM DICTIONARY:-
ser4={'m':'mango','b':'banana','c':'cherry','g':'grapes'}
s4=pd.Series(ser4)
print(s4)

#CREATING SERIES FROM TUPLE:-
ser5=('informatics practices','business.studs','economics','accounts'
      ,'english')
s5=pd.Series(ser5)
print(s5)

#SERIES ATTRIBUTES:-
fruits=["mango","apple","banana","cherry","grapes"]
fs=pd.Series(fruits)
print(fs)
print(fs.index)
print(fs.values)
print(fs.dtype)
print(fs.shape)
print(fs.nbytes)
print(fs.ndim)
print(fs.size)
print(fs.itemsize)
print(fs.hasnans)
print(fs.empty)
 

#PERFORMING METHAMETICAL OPERATIONS:-
s = pd.Series([1, 2, 3])
t = pd.Series ([1, 2, 4])
print(s)
print(t)
u=s+t  #addition operation
print(u)
v=s*t   #multiplication operation
print (v)

#FORMATION OF SERIES FROM METHAMETICAL OPERATIONS:-
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

print(ser1+ser2)
print(ser2-ser1)
print(ser1*ser2)
print(ser1/ser2)
print(ser4+ser3)
print(ser3*ser4)
print(ser3/ser4)
print(ser1+ser3) 

#PERFORMING VECTOR FUNCTIONS ON LIST:-
s=(11,12,13,14)
ser1=pd.Series(s)
print(ser1)
print(ser1+2)
print(ser1*3)
print(ser1/10)
print(ser1**2)
print(ser1>13)

#PERFORMING HEAD AND TAIL FUNCTIONS :-
s = pd.Series ([1, 2, 3, 4, 5], index =['a','b','c','d','e'])
print (s.head (3)) #FIRST 3 ELEMENTS
print (s.tail (3)) #LAST 3 ELEMENTS
                     ##########OR############
t=[1,2,3,4,5,6,7,8,9,10,11,12]
s=pd.Series(t,index=['a','b','c','d','e','f','g','h','i','j','k','l'])
print(s)
print(s.head())   #FIRST 5
print(s.tail())   #LAST 5
print(s.head(2))  #FIRST 2
print(s.tail(3))  #LAST 3

#write a program using selection loc()
l=([11,22,33,44,55,66])
s=pd.Series(l)
print(s)
print(s.loc[:2])  #FROM 0TH INDEX TO 2ND INDEX
print(s.loc[3:4]) #FROM 3RD INDEX TO 4TH INDEX
print(s.loc[2:2]) #ONLY 3ND INDEX(33) WILL PRINT
             ############OR#############
l=([11,22,33,44,55,66])
s=pd.Series(l,index=['k','a','n','u','j','i'])
print(s)
print(s.loc[:'u'])  #FROM kTH INDEX TO uND INDEX
print(s.loc['s':'d']) #FROM sRD INDEX TO dTH INDEX
print(s.loc['u':'u']) #ONLY sRD INDEX(33) WILL PRINT

###LOC------OF INT INDEX THEN ONLY INTEGER,
###LOC------OF STRING INDEX THEN MENTION THE STRING INDEX ONLY.
###ONLY SERIES NAME WRITTEN (NO LOC/ILOC) THEN ANYTHING....



#write a program using selection iloc()
l=([11,22,33,44,55,66])
s=pd.Series(l)
print(s)
print(s.iloc[:2])  #FROM 0TH INDEX TO 1ST INDEX(HIGHER VALUE-1)
print(s.iloc[3:4]) #FROM 3RD INDEX TO 3RD INDEX(HIGHER VALUE-1)
                ############OR##############
l=([11,22,33,44,55,66])
s=pd.Series(l,index=['k','a','n','u','j','i'])
print(s)
print(s.iloc[:2])  #FROM k INDEX TO h INDEX(HIGHER VALUE-1)
print(s.iloc[3:4]) #ONLY S INDEX(44)
print(s.iloc[2:3]) #ONLY sRD INDEX(33) WILL PRINT

###ILOC------OF INT INDEX THEN ONLY INTEGER,
###ILOC------OF STRING INDEX THEN ALSO MENTION INTEGER INDEX ONLY.
###ONLY SERIES NAME WRITTEN (NO LOC/ILOC) THEN ANYTHING....
'''















