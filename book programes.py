'''
import pandas as pd
a=pd.Series([1,2,7,5,4])
b=pd.Series([4,8,9,5,10])
print("first series is: ")
print(a)
print("second series is: ")
print(b)
print("comparing the elements of both the series")
print("equals")
print(a==b)
print("greater than: ")
print(a>b)
print("less than: ")
print(a<b)
print("adding two series:")
c=a+b
print(c)
print("subtracting two series: ")
c=a-b
print(c)
print("product of two series: ")
c=a*b
print(c)
print("divide series 1 by series 2 : ")
c=a/b
print(c)
'''
import pandas as pd
emp_data={"empid":[101,102,103,104,105,106,107,108,109,110],
          "ename":["khushi","vibhuti","kanishka","vandita","simar","harita","kiran","ishita","tanu","varundhawan"],
          "doj":["24-09-2004","13-08-2004","12-05-2005","14-06-2003","23-01-2001","6-03-2000","15-02-2008",""]}
df=pd.DataFrame(emp_data)
print(df)
print(df.head())









