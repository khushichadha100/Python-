
#write a program to print dataframe from given info:
import pandas as pd
dict={"name":["tom","jack","steve","ricky"],"age":[28,34,29,42]}
df=pd.DataFrame(dict)
print("*********************")
print("DATAFRAME DISPLAYED-:")
print(df)
print("*********************")


#write a program to print series and perform tail function:
import pandas as pd
l=["khushi","vibhuti","kanishka","vandita","simar","tanu",
   "lavanya","jessica","shourya","jahanvi"]
s=pd.Series(l)
print("******************")
print("SERIES DISPLAYED-:")
print(s)
print("TAIL FUNCTION USED TO RETRIEVE LAST 5 RECORDS-:")
print(s.tail())
print("***********************************************")


#write a program to make dataframe and then add a new column in the existing dataframe:
import pandas as pd
s= pd.Series([10,20,30,40]) 
df=pd.DataFrame(s) 
df.columns=["List1"] 
df["List2"]=50
print("***********************************************")
print("FIRST I CREATED LIST1 THEN ADDED LIST2 AND PRINTED THEM TOGETHER-:")
print(df)
print("***********************************************")

#Write a program to create a series with index=100,101,102,103:
import pandas as pd
empdata={"empid":[101,102,103,104],
         "ename":["khushi","vibhuti","kanishka","vandita"],
         "dob":["24-9-2004","13-8-2004","12-2-2004","06-09-2004"]}
df=pd.DataFrame(empdata)
df1=pd.DataFrame(empdata,index=[100,101,102,103])
print("***********************************************")
print("DATAFRAME DISPLAYED WITH SPECIFIED INDEX IN QUESTION-:")
print(df1)
print("***********************************************")

#Write a program to create 2 data frames and then take out their difference:
import pandas as pd
df1 = {'Subject':['semester1','semester2','semester3','semester4','semester1',
'semester2','semester3'],'Score':[62,47,55,74,31,77,85]}
df2 = {'Subject':['semester1','semester2','semester3','semester4'],'Score':[90,47,85,12]}
df1 = pd.DataFrame(df1,columns=['Subject','Score'])
df2 = pd.DataFrame(df2,columns=['Subject','Score'])
print("THIS IS DATAFRAME 1-:")
print(df1)
print("***********************************************")
print("THIS IS DATAFRAME 2-:")
print(df2)
set_diff_df = pd.concat([df2, df1, df1]).drop_duplicates(keep=False)
print("***********************************************")
print("HERE IS DIFFRENCE B/W THE TWO-:")
print(set_diff_df)
print("***********************************************")

#Write a program to create a series and then use loc and iloc function to retrieve values:
import pandas as pd
empdata={"empid":[101,102,103,104],"ename":["khushi","vibhuti","kanishka","vandita"],
"dob":["24-9-2004","13-8-2004","12-2-2004","13-9-2004"]}
df=pd.DataFrame(empdata)
print("HERE IS THE DATAFRAME-:")
print(df)
print("***********************************************")
print("RETREIVING VALUES USING LOC()<----<----<----<----<-----<----")
print(df.loc[:,:])#ALL COLUMNS ALL ROWS
print("***********************************************")
print(df.loc[0])#ALL COLUMNS 1 ROW
print("***********************************************")
print(df.loc[0:2])#ALL COLOUMNS MANY ROWS
print("***********************************************")
print(df.loc[:,"empid"])#ALL ROWS 1 COLUMN
print("***********************************************")
print(df.loc[:,"empid":"ename"])#ALL ROWS MANY COLUMN
print("***********************************************")
print(df.loc[1:4,"ename":"dob"])#MANY ROWS MANY COLUMNS
print("***********************************************")
print("RETREIVING VALUES USING ILOC()<----<----<----<----<-----<----")
print(df.iloc[:,:])#ALL COLUMNS ALL ROWS
print("***********************************************")
print(df.iloc[2:3,:])#ALL COLUMNS 1 ROW
print("***********************************************")
print(df.iloc[1:3,:])#ALL COLOUMNS MANY ROWS
print("***********************************************")
print(df.iloc[:,0])#ALL ROWS 1 COLUMN
print("***********************************************")
print(df.iloc[:,0:2])#ALL ROWS MANY COLUMN
print("***********************************************")
print(df.iloc[1:2,0:3])#MANY ROWS MANY COLUMNS
print("***********************************************")

#Write a program to create a series and then retrieve the values which are smaller than 5:
import pandas as pd 
s1=pd.Series([8,7,6,5,4,3,2,1])
print("***********************************************")
print("HERE TRUE IS WRITTEN INFRONT OF THE INDEX  WHERE VALUES ARE SMALLER THAN 5-:")
print(s1>5)
print("***********************************************")

#Write a program to create a dataframe and then use "pop" and "del" to delete the columns.
import pandas as pd
s = pd.Series([10,15,18,22]) 
df=pd.DataFrame(s)
df.columns=["List1"] 
df["List2"]=20  
df["List3"]=df["List1"]+df["List2"]
print("***********************************************")
print("PRINTING ALL LISTS-:")
print("***********************************************")
print(df)
print("***********************************************")
print("PRINTING OTHER LIST-:")
print(df[["List2"]])
print("***********************************************")
print("USING POP() TO DELETE COLUMN-:")
df.pop("List2")
print(df)
print("***********************************************")
print("USING DEL() TO DELETE COLUMN-:")
del df["List3"]
print(df)
print("***********************************************")

#Write a program to create a series and then multiply it by 4:
import pandas as pd
s = pd.Series([10,20,30,40,50,60,72,74])
print("***********************************************")
print("PRINTING ORIGINAL SERIES-:")
print(s)
print("***********************************************")
print("PRINTING THE SERIES AFTER MULTIPLYING BY 4-:")
print("***********************************************")
print(s*4)  
print("***********************************************")

#Write a program to create a series and perform head ( ) function and retrieve first 3 records:
import pandas as pd
empdata=['Sachin','Vinod','Lakhbir','Anil','Devinder','UmaSelvi']
df=pd.Series(empdata) 
print("***********************************************")
print("THIS IS THE SERIES-:")
print(df)
print("***********************************************")
print("RETRIEVING FIRST 3 RECORDS USING HEAD()-:")
print(df.head(3)) 
print("***********************************************")

#Write a program to create a series with 10 integers and sort them:
import pandas as pd
sr = pd.Series([19,16,22,2,1,12])
print("***********************************************")
print("THIS IS THE SERIES-:")
print("***********************************************")
print(sr)
print("***********************************************")
print("SORTING IN ASCENDING ORDER-:")
print("***********************************************")
s2=sr.sort_values(ascending = True)
print(s2)
s1=sr.sort_values(ascending = False)
print("***********************************************")
print("SORTING IN DESCENDING ORDER-:")
print("***********************************************")
print(s1)
print("***********************************************")
print("***********************************************")

#Write a Pandas program to compare the elements of the two Pandas Series:
s1=[12, 40, 61, 8, 10]
print("***********************************************") 
print("SERIES 1 -:")
print("***********************************************")
print(s1)
print("***********************************************")
print("SERIES 2 -:")
print("***********************************************")
s2=[1, 3, 5, 77, 90]
print(s2)
print("***********************************************")
print("COMPARING SERIES-:")
print(s1 == s2)
print("***********************************************")

#Write a program to create an empty series:
import pandas as pd
s=pd.Series() 
print("***********************************************")
print("EMPTY SERIES-:")
print(s)  
print("***********************************************")

#Write the python code to create both series given and also write the 
#command to display the product of series S1 and S2:
import pandas as pd
s1 = pd.Series([10,20,30,40,50,60,72,74]) 
s2=pd.Series([8,7,6,5,4,3,2,1])
print("***********************************************")
print("SERIES 1:")
print("***********************************************")
print(s1)
print("***********************************************")
print("SERIES 2 :")
print("***********************************************")
print(s2)
print("***********************************************")
print("DISPLAYING THEIR PRODUCT-:")
print("***********************************************")
print(s1*s2)
print("***********************************************")

#Write a program to create an empty dataframe:
import pandas as pd
s=pd.DataFrame()
print("***********************************************")
print("EMPTY DATAFRAME-:")
print(s)
print("***********************************************")
