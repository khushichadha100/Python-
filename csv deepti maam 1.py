import pandas as pd
def data_read():
    df=pd.read_csv('D:\DEEPTI DATA 2021\CLASS 12 INFO PRACTICES 2021-22\CSV FILES AND PROGRAMS\customer.csv')
    print(df)

data_read()

def data_selectedcols():
    df=pd.read_csv('D:\DEEPTI DATA 2021\CLASS 12 INFO PRACTICES 2021-22\CSV FILES AND PROGRAMS\customer.csv'
                   , usecols=['Name','City'])
    print(df)
    
#data_selectedcols()   


def data_selectedrows():
     df=pd.read_csv('D:\DEEPTI DATA 2021\CLASS 12 INFO PRACTICES 2021-22\CSV FILES AND PROGRAMS\customer.csv'
                    , nrows=2 , usecols=['Name','City'])
     print(df)
    
data_selectedcols()
data_selectedrows()



def data_withoutheader():
     df=pd.read_csv('D:\DEEPTI DATA 2021\CLASS 12 INFO PRACTICES 2021-22\CSV FILES AND PROGRAMS\customer.csv'
                    , header=None)
     print(df)
    
data_withoutheader()
def data_withnewcolumnnames():
     df=pd.read_csv('D:\DEEPTI DATA 2021\CLASS 12 INFO PRACTICES 2021-22\CSV FILES AND PROGRAMS\customer.csv'
                    , skiprows=1, names=['a','b','c'])
     print(df)  
     
data_withnewcolumnnames()

