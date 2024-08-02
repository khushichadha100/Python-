'''
#1ST:
import pandas as pd
series1=pd.Series([10,20,30,40])
print(series1)



#2ND:
import pandas as pd
empdata={"empid":[101,102,103,104],
         "ename":["khushi","vibhuti","kanishka","vandita"],
         "dob":["24-9-2004","13-8-2004","12-2-2004","13-9-2004"]}
df=pd.DataFrame(empdata)
df1=pd.DataFrame(empdata,index=["v1","v2","v3","v4",])#GIVING INDEXING
print(df1)



#3RD:
import pandas as pd
s=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(s)
print(s[0])
print(s[2:4])


#4TH:
import pandas as pd
empdata={"empid":[101,102,103,104],
         "ename":["khushi","vibhuti","kanishka","vandita"],
         "dob":["24-9-2004","13-8-2004","12-2-2004","13-9-2004"]}
df=pd.DataFrame(empdata)
print(df)
#####FORMAT==df.loc[startrow:endrow,startcolumn:endcolumn]
print(df.loc[0:2])#ALL COLOUMNS MANY ROWS
print(df.loc[:,"empid"])#ALL ROWS 1 COLUMN
print(df.loc[:,"empid":"ename"])#ALL ROWS MANY COLUMN
print(df.loc[1:4,"ename":"dob"])#MANY ROWS MANY COLUMNS




#5TH:
import pandas as pd
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "L&T":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=pd.DataFrame(runs)
print(df)
#####FORMAT==df.iloc[startrowindex:endrowindex,startcolumnindex:endcolumnindex]

print(df.iloc[:,:])#ALL COLUMNS ALL ROWS
print(df.iloc[2:3,:])#ALL COLUMNS 1 ROW
print(df.iloc[1:3,:])#ALL COLOUMNS MANY ROWS
print(df.iloc[:,0])#ALL ROWS 1 COLUMN
print(df.iloc[:,0:2])#ALL ROWS MANY COLUMN
print(df.iloc[1:2,0:3])#MANY ROWS MANY COLUMNS





#6TH:
import pandas as pd
l=[{'name':'khushi','surname':'chadha'},{'name':'vibhuti','surname':'gulati'},
{'name':'kanishka','surname':'kapoor'}]
df=pd.DataFrame(l)
print(df)   


#7TH:

import pandas as pd
empdata={ 'empid':[101,102,103,104,105,106],
'ename':['Sachin','Vinod','Lakhbir','Anil','Devinder','UmaSelvi'],
'Doj':['12-01-2012','15-01-2012','05-09-2007','17-01-2012'
       ,'05-09-2007','16-01-2012'] }
df=pd.DataFrame(empdata) 
print(df)
print(df.tail())
print(df.tail(2))





print(df.head())
print(df.head(2)) 



import pandas as pd
s = pd.Series([10,15,18,22]) 
df=pd.DataFrame(s)
df.columns=["List1"] 
df["List2"]=20  
df["List3"]=df["List1"]+df["List2"]
print(df)
print(df[["List2"]])
df.pop("List2")
print(df)
del df["List3"]
print(df)



import pandas as pd
ps1 = pd.Series([80, 25, 3, 25, 24, 6])
ps2 = pd.Series([80, 25, 3, 25, 24, 6])
  
print("Series1:")
print(ps1)
print("\nSeries2:")
print(ps2)
print("\nResult of comparing Two Series:")
result = ps1.equals(other=ps2)
print(result)


import pandas as pd
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "l&t":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=pd.DataFrame(runs)
print(df)
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


import pandas as pd
cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],
        'Year': [2015,2013,2018,2018]}
df = pd.DataFrame(cars, columns= ['Brand', 'Price','Year'])
df.sort_values(by=['Brand'], inplace=True)
print (df)
 





import pandas as pd
cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],
        'Year': [2015,2013,2018,2018]}
df = pd.DataFrame(cars, columns= ['Brand', 'Price','Year'])
df.sort_values(by=['Brand'], inplace=True,ascending=False)
print (df)






import pandas as pd
df1 = {'Subject':['semester1','semester2','semester3','semester4','semester1',
'semester2','semester3'],'Score':[62,47,55,74,31,77,85]}
df2 = {'Subject':['semester1','semester2','semester3','semester4'],
       'Score':[90,47,85,12]}
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
'''



import pandas as pd
empdata={"empid":[101,102,103,104],
         "ename":["khushi","vibhuti","kanishka","vandita"],
         "dob":["24-9-2004","13-8-2004","12-2-2004","13-9-2004"]}
df=pd.DataFrame(empdata)
print(df)
print(df.loc[:,:])#ALL COLUMNS ALL ROWS
print(df.loc[0])#ALL COLUMNS 1 ROW
print(df.loc[0:2])#ALL COLOUMNS MANY ROWS
print(df.loc[:,"empid":"ename"])#ALL ROWS MANY COLUMN
print(df.loc[1:4,"ename":"dob"])#MANY ROWS MANY COLUMNS



















 
























