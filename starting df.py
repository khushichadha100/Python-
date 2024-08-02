#starting with pandas::::::::::::::::::::::::::::::::::dataframe
'''
print("_________________________________________________________")
print("_________________________________________________________")
print("_________________________________________________________")
print("_________________________________________________________")

#write a program to convert datafram from series:
import pandas as pd
dic={'a':[1,2,3,4,5],'b':[6,7,8,9,10]}
df=pd.DataFrame(dic)
print(df.loc["1":"1",:])
#print(df[2:8])
#print(df[0:0])
print("_________________________________________________________")
print("_________________________________________________________")
print("_________________________________________________________")
print("_________________________________________________________")

#write a program to convert dataframe from list of dictionaries:
import pandas as pd
l=[{'name':'khushi','surname':'chadha'},{'name':'vibhuti','surname':'gulati'},
{'name':'kanishka','surname':'kapoor'}]
df=pd.DataFrame(l)                     
print(df)
print("__________________________________________________________")
print("__________________________________________________________")
print("__________________________________________________________")
print("__________________________________________________________")

#accessing data rows wise:
import pandas as pd
l=[{'name':'khushi','surname':'chadha'},{'name':'vibhuti','surname':'gulati'},
{'name':'kanishka','surname':'kapoor'}]
df=pd.DataFrame(l)
print(df)   
for(row_index,row_value)in df.iterrows():
   print("/n row index is:::",row_index)
   print("row value is:::")
   print(row_value)
print("___________________________________________________________")
print("___________________________________________________________")
print("___________________________________________________________")
print("___________________________________________________________")

#accessing data column wise:
import pandas as pd
l=[{'name':'khushi','surname':'chadha'},{'name':'vibhuti','surname':'gulati'},
{'name':'kanishka','surname':'kapoor'}]
df=pd.DataFrame(l)
print(df)   
for(col_name,col_value)in df.iteritems():
   print("/n column name is:::",col_name)
   print("column values is:::")
   print(col_value)
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")

#operations in dataframe:
import pandas as pd
empdata={"empid":[101,102,103,104],"ename":["khushi","vibhuti","kanishka",
"vandita"],"dob":["24-9-2004","13-8-2004","12-2-2004","13-9-2004"],"surname":["uihiug",
 "jhvftur","kgkyftdu","kkfyiftdusr"],"popyyy":[122,25365,272672,72762]}
df=pd.DataFrame(empdata)
print(df)
print(df.empid)
#######or#######
print(df["empid"])
print(df[["ename","dob","empid"]])
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")

#add,rename a coloumn in dataframe:
import pandas as pd
s = pd.Series([10,15,18,22]) 
df=pd.DataFrame(s)
df.columns=["List1"] 
df["List2"]=20  
df["List3"]=df["List1"]+df["List2"]  
print(df)
print(df[["List2"]])
del df["List3"]
print(df)
df.pop("List2")
print(df)
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")

#deleting specific coloumn or row:
import pandas as pd
s= pd.Series([10,20,30,40]) 
df=pd.DataFrame(s) 

df.columns=["List1"] 
df["List2"]=50
df1=df.drop("List2",axis=1) #to delete from column:(axis=1)

df2=df.drop(df.index[2],axis=0) #to delete from rows:(axis=0)
print(df2)

print(df1)#deleting list2
print(df2)#deleting 2 index of list1 and 2
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")

#deleting using inplace:
import pandas as pd
s= pd.Series([10,20,30,40]) 
df=pd.DataFrame(s) 
df.columns=["List1"] 
df["List2"]=50
print(df)
df1=df.drop("List2",axis=1,inplace=True)
df2=df.drop(df.index[[0,1]],axis=0,inplace=True)
print(df)
##INPLACE=TRUE(PRINT=ORIGINAL)
##INPLACE=FALSE(PRINT=VALUE WE HAVE GIVEN)

###########OTHER--------WAY#################
#program for iteration in dataframe:
import pandas as pd
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "l&t":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=pd.DataFrame(runs)
print(df)
print("____________________________________________________________")
#itering rows:
for (row,rowSeries) in df.iterrows():
    print("rowindex:",row)
    print("containing:")
    print(rowSeries)
#itering columns:
for (col,colSeries) in df.iteritems():
    print("coloumnindex:",col)
    print("containing:")
    print(colSeries)
print("_____________________________________________________________")
print("_____________________________________________________________")
print("_____________________________________________________________")
print("_____________________________________________________________")

#accessing df using loc()---CURLY IN CURLY:(dictionery in dictionery)
import pandas as pd
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "L&T":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=pd.DataFrame(runs)
print(df)
#####FORMAT==df.loc[startrow:endrow,startcolumn:endcolumn]
print(df.loc[:,:])#ALL COLUMNS ALL ROWS
print(df.loc["qtr3":,])#ALL COLUMNS 1 ROW
print(df.loc["qtr1":"qtr3":])#ALL COLOUMNS MANY ROWS
print(df.loc[:,"TCS"])#ALL ROWS 1 COLUMN
print(df.loc[:,"TCS":"L&T"])#ALL ROWS MANY COLUMN
print(df.loc["qtr1":"qtr2","TCS":"WIPRO"])#MANY ROWS MANY COLUMNS
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")

#accessing column and rows together loc()---SQAURE IN CURLY:(list in dictionery)
import pandas as pd
empdata={"empid":[101,102,103,104],
         "ename":["khushi","vibhuti","kanishka","vandita"],
         "dob":["24-9-2004","13-8-2004","12-2-2004","13-9-2004"]}
df=pd.DataFrame(empdata)
print(df)
print(df.loc[:,:])#ALL COLUMNS ALL ROWS
print(df.loc[0])#ALL COLUMNS 1 ROW
print(df.loc[0:2])#ALL COLOUMNS MANY ROWS
print(df.loc[:,"empid"])#ALL ROWS 1 COLUMN
print(df.loc[:,"empid":"ename"])#ALL ROWS MANY COLUMN
print(df.loc[1:4,"ename":"dob"])#MANY ROWS MANY COLUMNS
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")

#giving indexes explicitly in dataframe:
import pandas as pd
empdata={"empid":[101,102,103,104],
         "ename":["khushi","vibhuti","kanishka","vandita"],
         "dob":["24-9-2004","13-8-2004","12-2-2004","13-9-2004"]}
df=pd.DataFrame(empdata)
df1=pd.DataFrame(empdata,index=["v1","v2","v3","v4",])
print(df1)
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
'''
#accessing df using iloc()---CURLY IN CURLY:(dictionery in dictionery)
import pandas as pd
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "L&T":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=pd.DataFrame(runs)
print(df)
print(df.size)
#####FORMAT==df.loc[startrowindex:endrowindex,startcolumnindex:endcolumnindex]
'''
print(df.iloc[:,:])#ALL COLUMNS ALL ROWS
print(df.iloc[2:3,:])#ALL COLUMNS 1 ROW

print(df.iloc[1:3,:])#ALL COLOUMNS MANY ROWS
print(df.iloc[:,0])#ALL ROWS 1 COLUMN
print(df.iloc[:,0:2])#ALL ROWS MANY COLUMN
print(df.iloc[1:2,0:3])#MANY ROWS MANY COLUMNS

print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
'''
'''
#program using head and tail::
import pandas as pd
empdata={ 'empid':[101,102,103,104,105,106],
'ename':['Sachin','Vinod','Lakhbir','Anil','Devinder','UmaSelvi'],
'Doj':['12-01-2012','15-01-2012','05-09-2007','17-01-2012','05-09-2007','16-01-2012'] }
df=pd.DataFrame(empdata) 


print(df.head())
print(df.tail())
print("_________________________________________________________________")
print("_________________________________________________________________")
print("_________________________________________________________________")
print("_________________________________________________________________")
print(df.head(2)) 
print(df.tail(2))


print(df.iloc[["2","3"]])
print(df)
'''
















