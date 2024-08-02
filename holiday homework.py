'''
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
l=["khushi","vibhuti","kanishka","vandita","simar","tanu","lavanya","jessica","shourya","jahanvi"]
s=pd.Series(l)
print("******************")
print("SERIES DISPLAYED-:")
print(s)
print("***********************************************")
print("TAIL FUNCTION USED TO RETRIEVE LAST 5 RECORDS-:")
print(s.tail())
print("*******************")
'''
#write a program to make dataframe and then add a new column in the existing dataframe:
import pandas as pd
dict={"name":["tom","jack","steve","ricky"],"age":[28,34,29,42]}
df=pd.DataFrame(dict)
print("*********************")
df["age"]=90
print(df)
df1=df.drop(['name','age'])
print(df)

