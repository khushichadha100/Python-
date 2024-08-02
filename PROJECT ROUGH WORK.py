'''
import pandas as pd 
def data_selectedcols():
    df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                    ,index_col=0)
    print(df)
    
data_selectedcols()  

CONSUMER DISCRETIONARY
CONSUMER STAPLES
HEALTH CARE


password=input("ENTER PASSWORD TO ACCESS THIS PROGRAM : ")
if password =="pythonp":
    print("welcome !!")
else:
    print("!!!!!!!!!!!!!!!!!!!!")
    print("INVALID PASSWORD : ")
    print("!!!!!!!!!!!!!!!!!!!!")


#print('Enter correct username and password combo to continue')


count=1
while count<5:
  choice=int(input("enter-1,2,3,4-"))
   
  count+=1

import pandas as pd 
print("1. COMPANY NAME ")
print("2. COUNTRY ")
s2=int(input("enter from above 1 or 2 ?: "))
if s2 ==1:
     
     
    def data_selectedrows():
     df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv',usecols=['COMPANY NAME'])
     print(df)
    data_selectedrows()



import pandas as pd

A="COMPANY NAME"
B="COUNTY"
C="SECTOR"
DC=input("enter from above-")

 
def data_selectedcols():
     df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                 ,usecols=[DC])
     print(df)
data_selectedcols()  
if DC not in 'D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv':
 print("INVALID COLUMN !!")

if DC.isdigit():
 print("kkk")


def data_selectedrows():
     df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                    ,nrows=6,usecols=['COMPANY NAME','SECTOR'])
     print(df)
data_selectedrows()



import pandas as pd
def data_read():
 df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv')
 print(df)
data_read()


   
df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                 ,usecols=[DC])
print("invalid column ")
else: 
    def data_selectedcols():
    
    data_selectedcols()

import pandas as pd
SC=input("enter name of column - ")

if SC.isdigit() :
 print("INVALID COLUMN NAME- DIGIT NOT ALLOWED")

elif not SC in 'D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv':
 print("NOT FOUND ")
 
 

def data_selectedcols():
 df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                 ,usecols=['RANK'])
 print(df)
data_selectedcols()
def data_selectedcols():
         df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv',usecols=['RANK'])
         print(df)
data_selectedcols()



print("1. RANK")
print("2. COMPANY NAME")
print("3. COUNTRY")
print("4. SECTOR")
print("5. AR")
print("6. CVIM")
print("7. COMBINATION")
SC=int(input("ENTER THE NAME OF COLUMN FROM ABOVE -1 , 2 , 3 , 4 , 5 , 6 , 7 - "))
if SC==1:
 print("HERE IS YOUR DATA")
 print("***********************************")
 print("***********************************")
 def data_selectedcols():
  df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv',usecols=['RANK'])
  print(df)
 data_selectedcols()
 print("***********************************")
 print("***********************************")
elif SC==2:
       def data_selectedcols():
        df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                 ,usecols=['COMPANY NAME'])
        print(df)
       data_selectedcols() 
elif SC==3:
       def data_selectedcols():
        df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                 ,usecols=['COUNTRY'])
        print(df)
       data_selectedcols() 
elif SC==4:
       def data_selectedcols():
        df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                 ,usecols=['SECTOR'])
        print(df)
       data_selectedcols()
elif SC==5:
       def data_selectedcols():
        df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                 ,usecols=['AR'])
        print(df)
       data_selectedcols()   
elif SC==6:
       def data_selectedcols():
        df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv'
                 ,usecols=['CVIM'])
        print(df)
       data_selectedcols() 
elif SC==7:
       no_of_columns=int(input("ENTER THE NUMBER OF COLUMNS U WANT TO PRINT"))
       a=input("ENTER THE NAMES OF COLUMNS YOU WANT TO VIEW -")
       df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv')
       print(df[["a","b"]])


df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv')
print(df)
print("NOTE THAT-THESE ARE THE INDEXES OF EACH COLUMN :-")
print("0. RANK")
print("1. COMPANY NAME")
print("2. COUNTRY")
print("3. SECTOR")
print("4. AR")
print("5. CVIM")
print("6. COMBINATION")
SC=int(input("ENTER THE INDEX OF COLUMN FROM ABOVE - "))
SR=int(input("ENTER THE INDEX OF YOUR ROW - "))
SRT=int(input("ENTER THE ROW INDEX (+1) FROM WHERE YOU DON'T WANT RECORDS - "))
SCT=int(input("ENTER THE INDEX OF COLUMN (+1) FROM WHERE YOU DONT WANT COLUMNS - "))
print("NOTE !! - IF YOU ONLY WANT TO SEE 1 ROW AND 1 COLUMN THEN IN THE PLACE OF (SRT & SCT) YOU CAN INPUT (0)")
print(df.iloc[SR:SRT,SC:SCT]) 

service=input("ENTER YOUR DEMAND - 1 , 2 , 3 , 4 , 5 , 6 : ")
if service == 1:
    print("************************")
    print("HOW YOU WANT TO VIEW DATA ? ")
    print("CHOOSE FROM BELLOW : - ")
    print("************************")
    print("1. READ ALL AS DATAFRAME")
    print("************************")
    print("2. READ WITHOUT INDEX")
    print("************************")
    print("3. READ WITHOUT HEADER")
    print("************************")
    print("4. SUMMARY OF DATAFRAME")
    print("************************")
    print("5. EXIT")
    print("************************") 
else:
    print("invalid option")
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
COMPANIES=['US','SA','CHINA','SK','FRNC','SWTZLND','TAIWAN']
FREQUENCY=[20,1,4,1,1,2,1]
plt.bar(COMPANIES,FREQUENCY,color='k')
plt.title("COMPANIES INVOLVED IN RANKING")
plt.xlabel('COMPANIES')
plt.ylabel('FREQUENCY')
plt.show()
print("ABBREVIATIONS USED IN GRAPH:")
print(" 1) US_______________UNITED STATES")
print(" 2) SA_______________SAUDI ARABIA ")
print(" 3) SK_______________SOUTH KOREA")
print(" 4) FRNC_____________FRANCE")
print(" 5) SWTZLND__________SWITZERLAND")

COMPANIES=['US','SA','CHINA','SK','FRNC','SWTZLND','TAIWAN']
FREQUENCY=[20,1,4,1,1,2,1]

plt.hist(COMPANIES,FREQUENCY,color='k')
plt.title("COMPANIES INVOLVED IN RANKING")
plt.xlabel('COMPANIES')
plt.ylabel('FREQUENCY')
plt.show()   
'''
 print("NOTE THAT-THESE ARE THE INDEXES OF EACH COLUMN :-")
      print("0. RANK")
      print("1. COMPANY NAME")
      print("2. COUNTRY")
      print("3. SECTOR")
      print("4. AR")
      print("5. CVIM")
      print("6. COMBINATION")
      print("NOTE !! - IF YOU ONLY WANT TO SEE 1 ROW AND 1 COLUMN THEN IN THE PLACE OF (SRT & SCT) YOU CAN INPUT (0)")
      SC=int(input("ENTER THE INDEX OF COLUMN FROM ABOVE - "))
      SR=int(input("ENTER THE INDEX OF YOUR ROW - "))
      SRT=int(input("ENTER THE ROW INDEX FROM WHERE YOU DON'T WANT RECORDS (SRT) - "))
      SCT=int(input("ENTER THE INDEX OF COLUMN FROM WHERE YOU DONT WANT COLUMNS (SCT) - "))
      df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv')
      print(df[SR:SRT,SC:SCT]) 











