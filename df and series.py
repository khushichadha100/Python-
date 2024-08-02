'''
import pandas as pd
l=([11,22,33,44,55])
s=pd.Series(l,["1st","2nd","3rd","4th","5th"]) 
print(s)
print(s.loc[:'2nd'])
print(s.loc['3rd':'4th'])

#write a program using selection iloc()
import pandas as pd
l=([11,22,33,44,55])
s=pd.Series(l,["1st","2nd","3rd","4th","5th"]) 
print(s)
print(s.index)
 
'''
 
import pandas as class12
runs={"TCS":{"qtr1":25000,"qtr2":2000,"qtr3":3000,"qtr4":2000},
      "WIPRO":{"qtr1":28000,"qtr2":24000,"qtr3":36000,"qtr4":24000},
      "L&T":{"qtr1":21000,"qtr2":57000,"qtr3":35000,"qtr4":21000}}
df=class12.DataFrame(runs)
print(df.drop('qtr2',axis=0))








