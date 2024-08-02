
#SIMPLE PRINTING HELLO WORLD 
print("hello world")

#PROGRAM TO INPUT 2 NO. FROM USER AND DISPLAY THERE RESULT
a= int(input("enter no.1: "))
b= int(input("enter no.2: "))
c=a+b
print( "sum of a and b is =" ,c)

#CALCULATE AREA OF RECTANGLE
l=float(input("enter length: "))
b=float(input("enter breadth: "))
area=l*b
print("area is = " ,area)

#SQUARE/CUBE/ANY OTHER
num=int(input("enter no. :  "))
ex=int(input("enter no. raise to power :  "))
ans=num**ex
sq=num*num
cu=num*num*num
print("number raised to power is = ",ans)
print("square of the number is = ",sq)
print("cube of the no. is = ",cu)
 
#INTRO FOR YOURSELF
me=input("introduce yourself !\n")
print(me)

#2  NO.S FROM USER AND SWAP THEM
n1=int(input("enter no.1: "))
n2=int(input("enter no.2: "))
print("before swaping = ",n1,n2)
n1,n2=n2,n1
print("after swaping = ",n1,n2)

#3 NO.S SWAPING
n1=int(input("enter no.1: "))
n2=int(input("enter no.2: "))
n3=int(input("enter no.3: "))
print("before swaping = ",n1,n2,n3)
n1,n2,n3=n2,n3,n1
print("after swaping = ",n1,n2,n3)

#ASCII VALUES OF INPUTTED CHARACTERS
a=input("enter character\n")
print(ord(a))






