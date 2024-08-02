#TRYING NEW THINGS IN DATAFRAME::::::::(EXPLORING)
'''
print("---------DICTIONARY IN DICTIONARY---------------{{}}----------")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
'''
#CASE1::::::::::::::::ALL VALUES STRING DATAFRAME:
import pandas as pd
frnds={"name":{"n1":"khushi","n2":"vibhuti","n3":"kanishka","n4":"vandita"},
       "id":{"n1":1,"n2":2,"n3":3,"n4":4},
       "subject":{"n1":"ip","n2":"phys","n3":"eng","n4":"maths"}}
df=pd.DataFrame(frnds)
print("THIS IS A DATAFRAME:")
print(df)
'''
print("---------------6 CASES---------------------------")
print("CASE 1 : ALL COLUMNS ALL ROWS:-")
print(df.loc[:,:])
print("_________________________________________")
print("CASE 2 : ALL COLUMNS 1 ROW:-")
print(df.loc["n3":"n3",:])
print("_________________________________________")
print("CASE 3 : ALL COLOUMNS MANY ROWS:-")
print(df.loc["n1":"n3",:])
'''
print("_________________________________________")
print("CASE 4 : ALL ROWS 1 COLUMN:-")
print(df.loc[:,"name"])
'''
print("_________________________________________")
print("CASE 5 : ALL ROWS MANY COLUMN:-")
print(df.loc[:,"name":"id"])
print("_________________________________________")
print("CASE 6 : MANY ROWS MANY COLUMNS:-")
print(df.loc["n1":"n2","name":"id"])
print("_________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")

#CASE2::::::::::::::::COLUMN=STRING.......ROW=NUMERIC:
import pandas as pd
frnds={"name":{1:"khushi",2:"vibhuti",3:"kanishka",4:"vandita"},
       "id":{1:1,2:2,3:3,4:4},
       "subject":{1:"ip",2:"phys",3:"eng",4:"maths"}}
df=pd.DataFrame(frnds)
print("THIS IS A DATAFRAME:-")
print(df)
print("---------------6 CASES---------------------------")
print("CASE 1 : ALL COLUMNS ALL ROWS:-")
print(df.loc[:,:])
print("_________________________________________")
print("CASE 2 : ALL COLUMNS 1 ROW:-")
print(df.loc[3:3,])
print("_________________________________________")
print("CASE 3 : ALL COLOUMNS MANY ROWS:-")
print(df.loc[1:3,:])
print("_________________________________________")

print(df.loc[:,"name"])#ALL ROWS 1 COLUMN

print(df.loc[:,"name":"id"])#ALL ROWS MANY COLUMN

print(df.loc[1:2,"name":"id"])#MANY ROWS MANY COLUMNS
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")

#CASE3::::::::::::::::COLUMN=NUMERIC.......ROW=STRING:
import pandas as pd
frnds={1:{"n1":"khushi","n2":"vibhuti","n3":"kanishka","n4":"vandita"},
       2:{"n1":1,"n2":2,"n3":3,"n4":4},
       3:{"n1":"ip","n2":"phys","n3":"eng","n4":"maths"}}
df=pd.DataFrame(frnds)
print(df)
#---------------6 CASES---------------------------#

print(df.loc[:,:])#ALL COLUMNS ALL ROWS

print(df.loc["n3":"n3",])#ALL COLUMNS 1 ROW

print(df.loc["n1":"n3",:])#ALL COLOUMNS MANY ROWS

print(df.loc[:,1])#ALL ROWS 1 COLUMN

print(df.loc[:,1:2])#ALL ROWS MANY COLUMN

print(df.loc["n1":"n2",1:2])#MANY ROWS MANY COLUMNS
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
#CASE4::::::::::::::::COLUMN=NUMERIC.......ROW=NUMERIC:
import pandas as pd
frnds={1:{100:"khushi",200:"vibhuti",300:"kanishka",400:"vandita"},
       2:{100:1,200:2,300:3,400:4},
       3:{100:"ip",200:"phys",300:"eng",400:"maths"}}
df=pd.DataFrame(frnds)
print(df)
#---------------6 CASES---------------------------#

print(df.loc[:,:])#ALL COLUMNS ALL ROWS

print(df.loc[300:300,])#ALL COLUMNS 1 ROW

print(df.loc[100:300,:])#ALL COLOUMNS MANY ROWS

print(df.loc[:,1])#ALL ROWS 1 COLUMN

print(df.loc[:,1:2])#ALL ROWS MANY COLUMN

print(df.loc[100:200,1:2])#MANY ROWS MANY COLUMNS


print("--------------------LIST IN DICTIONARY--------------{[]}-----")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
#CASE1::::::::::::::::ALL VALUES STRING DATAFRAME:
import pandas as pd
frnds={"name":["khushi","vibhuti","kanishka","vandita"],
       "id":[1,2,3,4],
       "subject":["ip","phys","eng","maths"]}
df=pd.DataFrame(frnds)
print(df)
#---------------6 CASES---------------------------#

print(df.loc[:,:])#ALL COLUMNS ALL ROWS

print(df.loc[3:3,:])#ALL COLUMNS 1 ROW

print(df.loc[1:3,:])#ALL COLOUMNS MANY ROWS

print(df.loc[:,"name"])#ALL ROWS 1 COLUMN

print(df.loc[:,"name":"id"])#ALL ROWS MANY COLUMN

print(df.loc[1:2,"name":"id"])#MANY ROWS MANY COLUMNS
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
#CASE2::::::::::::::::COLUMN=STRING.......ROW=NUMERIC:
import pandas as pd
frnds={"name":[1,2,3,4],
       "id":[100,200,300,400],
       "subject":[10,20,30,40]}
df=pd.DataFrame(frnds)
print(df)
#---------------6 CASES---------------------------#

print(df.loc[:,:])#ALL COLUMNS ALL ROWS

print(df.loc[3:3,])#ALL COLUMNS 1 ROW

print(df.loc[1:3,:])#ALL COLOUMNS MANY ROWS

print(df.loc[:,"name"])#ALL ROWS 1 COLUMN

print(df.loc[:,"name":"id"])#ALL ROWS MANY COLUMN

print(df.loc[1:2,"name":"id"])#MANY ROWS MANY COLUMNS
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
#CASE3::::::::::::::::COLUMN=NUMERIC.......ROW=STRING:
import pandas as pd
frnds={1:["khushi","vibhuti","kanishka","vandita"],
       2:[1,2,3,4],
       3:["ip","phys","eng","maths"]}
df=pd.DataFrame(frnds,index=["1st","2nd","3rd","4th"])
print(df)

#---------------6 CASES---------------------------#

print(df.loc[:,:])#ALL COLUMNS ALL ROWS

print(df.loc["3rd":"3rd",:])#ALL COLUMNS 1 ROW

print(df.loc["1st":"3rd",:])#ALL COLOUMNS MANY ROWS

print(df.loc[:,1])#ALL ROWS 1 COLUMN

print(df.loc[:,1:2])#ALL ROWS MANY COLUMN

print(df.loc["1st":"2nd",1:2])#MANY ROWS MANY COLUMNS
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
print("______________________________________________________________")
#CASE4::::::::::::::::COLUMN=NUMERIC.......ROW=NUMERIC:
import pandas as pd
frnds={1:[100,200,300,400],
       2:[11,22,33,44],
       3:[100,200,300,400]}
df=pd.DataFrame(frnds)
print(df)
#---------------6 CASES---------------------------#

print(df.loc[:,:])#ALL COLUMNS ALL ROWS

print(df.loc[3:3,:])#ALL COLUMNS 1 ROW

print(df.loc[1:3,:])#ALL COLOUMNS MANY ROWS

print(df.loc[:,1])#ALL ROWS 1 COLUMN

print(df.loc[:,1:2])#ALL ROWS MANY COLUMN

print(df.loc[1:2,1:2])#MANY ROWS MANY COLUMNS
'''

















































