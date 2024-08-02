def submenu1():
    print("           __________________________________                       ")
    print("              ************************")
    print("                 HERE'S YOUR DATA:-")
    print("                                                                      ")
    print("TITLE - WORLD LARGEST COMPANIES ON THE BASIS OF MARKET CAPITALIZATION")
    print(".....................................................................")
    df=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv')
    print (df)  
    print("                                                                   ")
    print("                                                                   ")
    print("ABBREVIATIONS USED IN COLUMNS ARE : -")
    print("________________________________________")
    print(" AR - ANNUAL REVENUE ")
    print(" CVIM - CAPITALIZED VALUE IN MARKET ")
    print("________________________________________")
    print("                                           ")
    #print("***********************************")
    print("ABBREVIATIONS USED IN (SECTOR) COLUMN :-")
    #print("............................")
    print("1) CONSUMER DISCRETIONARY : CD")
    #print("............................")
    print("2) CONSUMER STAPLES : CS")
    #print("............................")
    print("3) HEALTH CARE : HC")
    #print("............................")
    print("___________________________________________________________")
    print("                                                                    ")

def submenu2():
     print("           __________________________________                       ")
     print("              ************************")
     print("                HERE IS YOUR DATA")
     print("                                                            ")
     #print("***********************************")
     df3=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv')
     df3.info()  
     print("_________________________________________________________")
     print("                                                                   ")
def submenu3():
    print("           __________________________________                       ")
    print("              ************************")
    print("                HERE IS YOUR DATA : ")
    print("                                                                   ")
    #print("***********************************")
    df4=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv')
    print(df4.head())
    print('____________________________________________________________')
    print("                                                                   ")
    #print("***********************************")
def submenu4():
    print("           __________________________________                       ")
    print("              ************************")
    print("                HERE IS YOUR DATA : ")
    print("                                                            ")
    #print("***********************************")
    df5=pd.read_csv('D:\khushi XII\OTHERSSSSS\IP CSV WORK (ALL)\IP.csv')
    print(df5.tail())
    print('____________________________________________________________')
    print("                                                                   ")
    #print("***********************************")
def submenu5():
    print("           __________________________________                       ")
    print("********************************")
    print("                                                                   ")
    CVIM=[12.1,1.9,1.8,1.6,1.4]
    COMPANY=['APPLE','SAUDI ARMCO','MICRO.','AMAZON','ALPHABET']
    plt.plot(CVIM,COMPANY,marker="*",color='m',linestyle=':')
    plt.title("TOP 5 COMPANIES ANALYSIS BASED ON THEIR CAPITALIZED VALUE IN MARKET")
    plt.xlabel("CVIM IN $T")
    plt.ylabel("COMPANY NAME")
    plt.show()
    print('____________________________________________________________')
    print("                                                                   ")
def submenu6():
    print("           __________________________________                       ")
    print("********************************")
    print("                                                                   ") 
    CVIM=[12.1,1.9,1.8,1.6,1.4]
    COMPANY=['APPLE','SAUDI ARMCO','MICRO.','AMAZON','ALPHABET']
    plt.bar(COMPANY,CVIM)
    plt.title("TOP 5 COMPANIES ANALYSIS BASED ON THEIR CAPITALIZED VALUE IN MARKET")
    plt.xlabel("COMPANY")
    plt.ylabel("CVIM")
    plt.show()
    print('____________________________________________________________')
    print("                                                                   ")
def submenu7():
    print("           __________________________________                       ")
    print("********************************")
    print("                                                                   ") 
    CVIM=[12.1,1.9,1.8,1.6,1.4]
    COMPANY=['APPLE','SAUDI ARMCO','MICRO.','AMAZON','ALPHABET']
    plt.barh(COMPANY,CVIM)
    plt.title("TOP 5 COMPANIES ANALYSIS BASED ON THEIR CAPITALIZED VALUE IN MARKET")
    plt.xlabel("COMPANY")
    plt.ylabel("CVIM")
    plt.show()
    print('____________________________________________________________')
    print("                                                                   ")
def submenu8():
    print("           __________________________________                       ")
    print("********************************")
    print("                                                                   ") 
    data=('APPLE','SAUDI ARMCO','MICRO','AMAZON','ALPHABET')
    plt.hist(data,weights=[12.1,1.9,1.8,1.6,1.4],color ='c',edgecolor='k')
    plt.title("TOP 5 COMPANIES ANALYSIS BASED ON THEIR CAPITALIZED VALUE IN MARKET")
    plt.xlabel("COMPANY")
    plt.ylabel("CVIM")
    plt.show()
    print('____________________________________________________________')
    print("                                                                   ")


def choicemenu1():
     print("                                                                   ")
     print("                *************************") 
     print("                HOW YOU WANT TO VIEW DATA ? ")
     print("                  CHOOSE FROM BELLOW : - ")
     print("                                                                  ")
     print("                 1.READ ALL AS DATAFRAME        ")
     print("                 ---------------------------------                        ")
     #print("************************")
     print("                 2.SUMMARY OF DATAFRAME         ")
     print("                 ---------------------------------                        ")
     #print("************************")
     print("                 3.EXIT                         ")
     print("                  ---------------------------------                        ")
     #print("************************")
     S1=int(input('ENTER YOUR DEMAND - 1, 2 , 3 :'))
     if S1==1:
         submenu1()
         choicemenu1()
     elif S1==2: 
         submenu2()
         choicemenu1()
     elif S1==3:
         print("........................................")
         print("OKAY , EXITING !!")
         print('____________________________________________________________')
         print("                                                                   ")
         mainmenu1()
     else:
         #print("!!!!!!!!!!!!!!!!!!")
         print("INVALID OPTION !!")
         print('____________________________________________________________')
         print("                                                                   ")
         mainmenu1()
def choicemenu2():
     print("                                                                   ")
     print("                  ************************")
     print("               HOW YOU WANT TO VIEW RECORDS ? ")
     print("                    CHOOSE FROM BELLOW : - ")
     print("                                                                        ")    
     print("               1.VIEW FIRST 5 RECORDS WITH ALL COLUMNS")
     print("              --------------------------------------------                   ")
     #print("*********************************************")
     print("               2.VIEW LAST 5 RECORDS WITH ALL COLUMNS")
     print("               -------------------------------------------                  ")
     #print("*********************************************")  
     print("               3.EXIT")    
     print("              ---------------------------------------------           ")
     #print("*********************************************")
     S2=int(input("ENTER YOUR CHOICE - 1 , 2 , 3 : "))
     if S2==1:
         submenu3()
         choicemenu2()
     elif S2==2:
         submenu4()
         choicemenu2()
     elif S2==3:
         print("........................................")
         print("OKAY , EXITING !!")
         print('____________________________________________________________')
         print("                                                                   ")
         mainmenu1()
     else:
         #print("!!!!!!!!!!!!!!!!!!")
         print("INVALID OPTION !!")
         print('____________________________________________________________')
         print("                                                                   ")
         mainmenu1()
          
         
def choicemenu3():
     print("                                                                   ")
     print("                ************************")
     print("                 HOW YOU WANT TO VIEW ? ")
     print("                  CHOOSE FROM BELLOW : - ")
     print("                                                                 ")       
     print("                    1.LINE GRAPH")
     print("                ---------------------------------                        ")
     #print("........................................")
     print("                    2.BAR GRAPH")
     print("               ---------------------------------                        ")
     #print("........................................") 
     print("                    3. HORIZONTAL BAR GRAPH")
     print("               ---------------------------------                        ")
     #print("*********************************************") 
     print("                    4.HISTOGRAM")    
     print("               ---------------------------------                        ")
     #print("*********************************************")
     print("                    5.EXIT")
     print("                ---------------------------------                        ")
     S3=int(input("ENTER YOUR CHOICE - 1 , 2 , 3 ,4 ,5 : "))
     if S3==1:
         submenu5()
         choicemenu3()
     elif S3==2:
         submenu6()
         choicemenu3()
     elif S3==3:
         submenu7()
         choicemenu3()
     elif S3==4:
         submenu8()
         choicemenu3()
     elif S3==5:
         print("........................................")
         print("OKAY , EXITING !!")
         print('____________________________________________________________')
         print("                                                                   ")
         mainmenu1()
     else:
         #print("!!!!!!!!!!!!!!!!!!")
         print("INVALID OPTION !!")
         print('____________________________________________________________')
         print("                                                                   ")
         mainmenu1()
         
count=0
while count<3:
    password=input("ENTER PASSWORD TO ACCESS THIS PROGRAM : ")
    if password=='pythonp' or password=='PYTHONP':
        count=4
        print("                                                            ")
        print('                    ***ACCESS GRANTED***')
        print('____________________________________________________________')
        print('____________________________________________________________')
        print("                                                                   ")
        
    else:
        print("                                                      ")
        print('                     ***ACCESS DENIED***')
        print('____________________________________________________________')
        print('____________________________________________________________')
        print("                                                                   ")
        count+=1
        
import sys as sys
import pandas as pd
import matplotlib.pyplot as plt
def mainmenu1():
            #print("*****************************************************************")
            print("             WELCOME , HOW MAY I HELP YOU ? ")
            print("                                                                  ")
            #print("*****************************************************************")
            print("         FOLLOWING ARE THE SERVICES WHICH I CAN PROVIDE YOU !!")
            print("                                                                   ")
            #print("*****************************************************************")
            print("                  CHOOSE FROM BELLOW !!")
            print("                                                                  ")
            print("                ~~~~~~~ MAIN MENU ~~~~~~~                           ")
            print("                                                                  ")
            #print(".................................................................")
            print("                 1.   FETCH DATA")
            print("             __________________________________                       ")
            #print(".................................................................")
            print("                 2.   ACCESS ROWS AND COLUMNS")
            print("             __________________________________                       ")
            #print(".................................................................")
            print("                 3.   VIEW VISUALIZED DATA")
            print("             __________________________________                       ")
            #print(".................................................................")
            print("                 4.   EXIT")
            print("             __________________________________                       ")
            #print(".................................................................")
            choice=int(input("ENTER YOUR DEMAND - 1, 2 , 3 , 4 : "))
            if choice ==1:
                choicemenu1()
            elif choice==2:
                choicemenu2()
            elif choice==3:
                choicemenu3()
            elif choice==4:
                #print("*******************")
                print("                                                                   ") 
                print("----------------------------------------------------------")
                print("                  HAVE A GOOD DAY !")
                print("----------------------------------------------------------")
                sys.exit()
mainmenu1()      
    