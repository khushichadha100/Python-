
import pandas as pd 
s = pd.Series([10,20,30,40,50,60,72,74],index=['a','b','c','d','e','f','g','h']) 
s1=pd.Series([8,7,6,5,4,3,2,1], index=['a','b','c','d','e','f','g','h']) 
print(s.iloc[2:5])
print("\n indexes in series are :::")
print(s.index)

s['c']+20 
print(s)
print(s*10)
print(s!=35) 
s['a']=5 
print(s) 
print(s-s1) 
print(s[s<40]) 
print(s1['c']) 
print(s1[ : :-1]) 
print(s[2:]) 
print(s[: : 2])
s['d']=s['d']+200 
print(s['d'])
print(s[ : 4]) 
print(s1>2) 
print(s1[: : -2])
print(s*s1)
'''
import pandas as pd
dict={"Icode":['A21','B26','B35','C80','A30'],
   "Item":["frock","cot","soft toy","baby socks","baby suit"],
   "Date-Purchase":["2016-01-23","2015-09-23","2016-06-17","2014-10-16","2015-09-20"],
   "Unit Price":[700,5000,800,100,500],
   "Discount":[10,25,10,7,5] }
df=pd.DataFrame(dict)
print(df.loc[4])
df1=pd.DataFrame(dict,index=[10,20,30,40,50])
print(df1)

#print(df.loc[3:3,:])
#print(df[["Unit Price","Discount"]])

#print(df.head(3))
#print(df.tail(4))
#print(df.loc[2:4,'Unit Price':])
#df1["qual"]="a+"
#print(df1)
#del df1["Item"]
#df1.pop("Discount")
print(df1.loc[[20,40],["Unit Price","Discount"]])
#print(df2)

 
#print(df1.loc[1:3,"Unit Price": ])
'''



