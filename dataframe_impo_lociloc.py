import pandas as pd
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "L&T":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=pd.DataFrame(runs)
print(df)

#####FORMAT==df.loc[startrow:endrow,startcolumn :endcolumn ]
'''
print(df.iloc[0:,-3:-1])
print(df.iloc[:,:])#ALL COLUMNS ALL ROWS
print(df.iloc[2:3,:])#ALL COLUMNS 1 ROW

print(df.iloc[1:3,:])#ALL COLOUMNS MANY ROWS
print(df.iloc[:,0])#ALL ROWS 1 COLUMN
print(df.iloc[:,0:2])#ALL ROWS MANY COLUMN
print(df.iloc[1:2,0:3])#MANY ROWS MANY COLUMNS

import pandas as pd
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "L&T":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=pd.DataFrame(runs)
print(df)
'''
#####FORMAT==df.loc[startrow:endrow,startcolumn:endcolumn]
print(df.loc[:,:])#ALL COLUMNS ALL ROWS
print(df.loc["qtr3":'qtr4',:])#ALL COLUMNS 1 ROW
print(df.loc["qtr1":"qtr3":])#ALL COLOUMNS MANY ROWS
print(df.loc[:,"TCS"])#ALL ROWS 1 COLUMN
print(df.loc[:,'TCS':'WIPRO'])#ALL ROWS MANY COLUMN
print(df.loc["qtr1":"qtr2","TCS":"WIPRO"])#MANY ROWS MANY COLUMNS
 
