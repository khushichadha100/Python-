import pandas as pd
                   #  0,  1,  2,  3,  4,  5
l=                  ([11,22, 33, 44, 55, 66])
s=pd.Series(l,index=['k','a','n','u','j','i'])
                   # -6 ,-5, -4, -3 ,-2 , -1
print(s)
'''
#print(s.loc[:2])  #FROM 0TH INDEX TO 2ND INDEX
#print(s.loc[3:4]) #FROM 3RD INDEX TO 4TH INDEX
print(s[0])       #ONLY 0TH INDEX
print(s[0:5])    #FROM 0TH INDEX TO 4TH INDEX(HIGHER VALUE-1)
#print(s.loc[2:2]) #ONLY 3ND INDEX(33) WILL PRINT
            

print(s.loc[:'u'])  #FROM kTH INDEX TO uND INDEX
print(s.loc['s':'d']) #FROM sRD INDEX TO hTH INDEX

print(s['k'])       #ONLY 11 WILL PRINT------
              #####OR#####                   SAME OUTPUT=11
print(s[0])         #ONLY 11 WILL PRINT------

print(s[0:5])    #FROM kTH INDEX TO hTH INDEX(HIGHER VALUE-1)
print(s.loc['u':'u']) #ONLY sRD INDEX(33) WILL PRINT


###LOC------OF INT INDEX THEN ONLY INTEGER,
###LOC------OF STRING INDEX THEN MENTION THE STRING INDEX ONLY.
###ONLY SERIES NAME WRITTEN (NO LOC/ILOC) THEN ANYTHING....

'''

 
print(s.iloc[:2])  #FROM 0TH INDEX TO 1ST INDEX(HIGHER VALUE-1)
print(s.iloc[3:4]) #FROM 3RD INDEX TO 3RD INDEX(HIGHER VALUE-1)
'''
print(s.iloc[:2])  #FROM k INDEX TO h INDEX(HIGHER VALUE-1)
print(s.iloc[3:4]) #ONLY S INDEX(44)

print(s['k'])       #ONLY 11 WILL PRINT------
              #####OR#####                   SAME OUTPUT=11
print(s[0])         #ONLY 11 WILL PRINT------

print(s[0:5])    #FROM kTH INDEX TO hTH INDEX(HIGHER VALUE-1)
print(s.iloc[2:3]) #ONLY sRD INDEX(33) WILL PRINT

###ILOC------OFINT INDEX THEN ONLY INTEGER,
###ILOC------OF STRING INDEX THEN ALSO MENTION INTEGER INDEX ONLY.
###ONLY SERIES NAME WRITTEN (NO LOC/ILOC) THEN ANYTHING....
 

print(s[:-4]) #FROM 0 INDEX(K) TO -5 INDEX(H) (HIGHER VALUE-1)
print(s[-3])  #ONLY 44 WILL PRINT AT (-3)INDEX
print(s[-6:-4]) #FROM -6 INDEX(11) TO -5 INDEX(22) (HIGHER VALUE-1)

print(s.iloc[:2])  #FROM k INDEX TO h INDEX(HIGHER VALUE-1)
print(s.iloc[3:4]) #ONLY S INDEX(44)

print(s['k'])       #ONLY 11 WILL PRINT------
              #####OR#####                   SAME OUTPUT=11
print(s[0])         #ONLY 11 WILL PRINT------

print(s[0:5])    #FROM kTH INDEX TO hTH INDEX(HIGHER VALUE-1)
print(s.iloc[2:3]) #ONLY sRD INDEX(33) WILL PRINT


'''


















