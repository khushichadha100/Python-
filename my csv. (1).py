
import pandas as pd
'''
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


def data_selectedrows():
     df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\stud.csv'
                    ,nrows=2,usecols=['STUDENTS','SUBJECTS ONLY'])
     print(df)
data_selectedrows()
 

def data_withoutheader():
     df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\stud.csv'
                    , header=None)
     print(df)
data_withoutheader()    

'''
def data_withnewcolumnnames():
     df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\stud.csv'
                    , skiprows=1, names=['a','b','c'])
     print(df)  
     
data_withnewcolumnnames()




