import pandas as pd
'''
#CREATING EMPTY DATAFRAME:-
df=pd.DataFrame()
print(df)

#CREATING LIST FROM DATAFRAME:- AND NAMING THE COLUMN NAME:-
df=['kanuji','kanha','maakhan chor','murlidhar','govind']
df1=pd.DataFrame(df,columns=['KHUSHI K SHYAAM'])
print(df1)

#CREATING DATAFRAME FROM 2 LISTS:-
dic={'a':[1,2,3,4,5],'b':[6,7,8,9,10]}
df=pd.DataFrame(dic)
print(df)

#CREATING DATAFRAME FROM NESTED LIST:-
data=[['khushi','chadha'],['krishna','vasudev yadav']]
df2=pd.DataFrame(data,columns=['name','surname'])
print(df2)

#CREATING DATAFRAME FROM SERIES:-
marks=pd.Series({'vijay':34,'rahul':50,'meghna':19})
age=pd.Series({'vijay':12,'rahul':15,'meghna':14})
df3=pd.DataFrame({'marks':marks,'age':age})
print(df3)

#CREATING DATAFRAME FROM DICTIONARY:-
############################################################################
#1.LIST OF DICTIONARIES::::::::::::
l=[{'name':'khushi','surname':'chadha'},{'name':'vibhuti','surname':'gulati'},
{'name':'kanishka','surname':'kapoor'}]
df=pd.DataFrame(l)                     
print(df)

############################################################################
#2. DICTIONARY OF LIST::::::::::::::::::
k={'kanha':['kanuji','murlidhar','shyaam','mohan'],
   'khushi':['kanha daasi ','kanha laadli','kanha sakhi','kanha priya']}
dfk=pd.DataFrame(k)
print(dfk)

############################################################################
#3. DICTIONARY OF SERIES:::::::::::::::::::
empdata={"empid":pd.Series([101,102,103,104]),
         "ename":pd.Series(["khushi","vibhuti","kanishka","vandita"]),
         "surname":pd.Series(["chadha","gulati","kapoor","soni"]),
         "dob":pd.Series(["24-9-2004","13-8-2004","12-2-2004","13-9-2004"])}
df=pd.DataFrame(empdata)
print(df)

#SELECTING AND ACCESSING RECORDS FROM DATAFRAME:-
empdata={"empid":pd.Series([101,102,103,104]),
         "ename":pd.Series(["khushi","vibhuti","kanishka","vandita"]),
         "surname":pd.Series(["chadha","gulati","kapoor","soni"]),
         "dob":pd.Series(["24-9-2004","13-8-2004","12-2-2004","13-9-2004"])}
df=pd.DataFrame(empdata)
print(df)
print(df.empid)
                 #######or#######
print(df["empid"])
print(df[["dob","empid","ename"]])
print(df[::-2])  #HIGHER VALUE-1
print(df[:3])   #HIGHER VALUE-1

#ADDING,ACCESSING,DEL/POP/DROP:-
import pandas as pd
s = pd.Series([10,15,18,22]) 
df=pd.DataFrame(s)
df.columns=["List1"] 
df["List2"]=20        #NEW LIST/COLUMN ADDED WITH CONSTANT VALUE
df["List3"]=df["List1"]+df["List2"]  
print(df)
print(df.List1)
#########OR###########
print(df['List1'])
print(df[["List2","List3"]])

del df["List3"]
print(df)

df2=df.pop("List2")
print(df)
print(df2) #LIST 2 WILL POP OUT

#AXIS=0=ROW-WISE
#AXIS=1=COLUMN-WISE
df2=df.drop(index=[3],axis=0)
print(df2)
df3=df.drop('List1',axis=1)
print(df3)
'''
#ATTRIBUTES OF DATAFRAME:-
import pandas as pd
stud={'name':['rinku','ritu','ajay','pankaj','aditya'],
       'english':[67,78,75,88,92], 'economics':[78,67,89,90,56],
     'ip': [78,88,98,90,87],'accounts': [77,70,80,67,86]}
studdf=pd.DataFrame(stud,index=['r','t','a','p','d'])
print(studdf)
print(studdf.index)  #RETURNS ALL INDEX NAMES
'''
print(studdf.columns) #RETURNS ALL COLUMN NAMES
print(studdf.axes)    #1.ROWINDEX LABELS 2.THEN COLUMN INDEX LABELS
print(studdf.dtypes)  #ALL COUMNS DATATYPES
print(studdf.size)     #NO. OF ROWS * NO. OF COLUMNS
print(studdf.shape)    #NO.OF ROWS , NO. OF COLUMNS
print(studdf.ndim)
print(studdf.empty)
print(studdf.count(1)) #all index and infront of them no. of columns
print(studdf.count(0))  #all columns names infront of them no. of row indexes
print(studdf.T)          #interchanges columns index and rows index


#ITERATION OF ROWS AND COLUMNS:-
import pandas as pd
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "l&t":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=pd.DataFrame(runs)
print(df)
print("____________________________________________________________")
#itering rows:

for (row,rowSeries) in df.iterrows():
   # print("rowindex:",row)
   # print("containing:")
    print(rowSeries)

#itering columns:
for (col,colSeries) in df.iteritems():
   # print("coloumnindex:",col)
   # print("containing:")
    print(colSeries)

#HEAD AND TAIL :-
empdata={ 'empid':[101,102,103,104,105,106],
'ename':['Sachin','Vinod','Lakhbir','Anil','Devinder',
         'UmaSelvi'],
'Doj':['12-01-2012','15-01-2012','05-09-2007','17-01-2012'
       ,'05-09-2007','16-01-2012'] }
df=pd.DataFrame(empdata) 
print(df)

print(df.head())
print(df.tail())
print(df.head(2)) 
print(df.tail(2))

import pandas as pd
s = pd.Series([10,15,18,22]) 
df=pd.DataFrame(s)
df.columns=["List1"]    #RENAMING A COLUMN
print(df)

df["List2"]=20        #NEW LIST/COLUMN ADDED WITH CONSTANT VALUE
df["List3"]=df["List1"]+df["List2"]  
print(df)
df.loc[4]=90             #ADD ROW.....(.LOC)
print(df)
df["List5"]=[23,56,89,35,90]   #ADD COLUMN.....[COLUMN NAME]
print(df)
'''
#CSV RELATED:-
#TO READ THE CSV FILE IN DATAFRAME FORMAT
def data_read():
    df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\stud.csv')
    print(df)
data_read() 


#TO SEE A PARTICUAR COLUMN(S) USING (USECOLS):
def data_selectedcols():
    df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\stud.csv'
                   ,usecols=['STUDENTS','SN'])
    print(df)
data_selectedcols()  

#TO SEE PARTICULAR ROWS OR COLUMNS:-
def data_selectedrows():
     df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\stud.csv'
                    ,nrows=2,usecols=['STUDENTS','SUBJECTS ONLY'])
     print(df)
data_selectedrows()





