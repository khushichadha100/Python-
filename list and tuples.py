'''
list1 = ['Red','Green','Blue','Yellow', 'Black']
for item in list1:
 print(item,end=',')
#Or

print("\n*******")

for i in range(len(list1)):
 print(list1[i]) 
print("\n*******")
list1 = ['Red','Green','Blue','Yellow','Black']
i = 0
while i < len(list1):
 print(list1[i])
 i += 1


multiples=[x*7 for x in range(1,11)]
print(multiples)

 
#x= [int(x) for x in input().split()]
#print(x)

list1 = ['Red','Green','Blue']
print('Green' in list1)#True
print('Cyan' in list1) #False


list1 = [34,12,6,3,92,44]
print(max(list1))
print(min(list1))

L=[500,1000,1500,2000]
l1=[50,60]
L.extend(l1)
print(L)

L=[500, 1000, 1500, 2000, 2500, 3000, 3500]
print (L)
L.pop()  # removes the last element
print (L)
L.pop(2)
print (L)
del L[2]


l=[3000, (2500, 2800),600, {1500:'a'}, 500]
 
print (l)
 

mytple=("admin",5,7,[1,2,3],(2,4,6))
print(mytple[0])
print(mytple[1])
print(mytple[2])

print(mytple[3][1])

print("\n****")
mtup=("admin","arjun","harleen")
for x in mtup:
 print("hello " + x) 

print("\n****")

mtup=("admin","arjun","harleen")
for i in range(len(mtup)):
 print(("hi "+ mtup[i]))

print("\n****")

i=0
while (i<len(mtup)):
 print("yo "+ mtup[i] + ' do')
 i+=1

list1=list(mtup)
print(list1)
list1[0]='khushi'
mtup=tuple(list1)
print(mtup)


t=("cat","dog","bear","pig","bull")
print(min(t))
print(max(t))
 
'''
tup1=(1,2,3)
tup2=(10,20,30,40,50,60)
print(tup1+tup2)   
print(tup1*3)   
print(tup1[0])
print(tup2[1:])
print(tup1[::-1])
print(tup1[2:5])
print(tup2[::2])

'''
my=('p','q','r','r','s')
print(my.count('r'))
print(my.count('s'))
print(my.count('a'))
print(my.index('r'))

#print(my.index('k'))
#print(my.count('k'))

Tuple1=(2,3,2,2,3)
i=1 #anything multiply with 0 will be zero, i=1
for x in Tuple1:
 i*=x
print("final:",i)
 '''




