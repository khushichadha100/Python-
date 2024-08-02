'''
l=[10,20,30,40]
print(l)
l[0]=l[0]+2
print(l)
print(l[::-1])
l[1]=50
print(l)
l=l*2
print(l)


tup=(3,)
tupp=(4,5,6)
t3=tup+tupp
print(t3)


def add(a,b,c):
    print(a+b+c)
c=add(6,16,26)
'''
car ={
"brand": "Ford",
"model": "Mustang",
'colors':{'1st':'red','2nd':'blue'},
"engine":{1:777,2:888,3:779},
"year": 1964
}
print(car)
'''
print(car['brand'])
print(car['colors'])
print(car['colors']['2nd'])
print(len(car))
 
str1=str(car)
print(str1)

print(car.keys())
print(car.values())

print(car.items())
print(car.get('model'))
print(car.get('colors'))
#print(car[1])
print(car['model'])
#print(car['khushi'])#key error
print(car.get('model'))
print(car.get('khushi'))
car.update({'year':2020})
print(car)
#del car ["dhgcgel"]
#car.pop('hvchvc')
'''
for x, y in car.items():
     print(x, y) 
     
if 'rs' not in car:
    print('no')
#squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} # create a dictionary
# remove a particular item, returns its value 
##print(car.pop('year'))
# Output: 16
#print(car) 
# Output: {1: 1, 2: 4, 3: 9, 5: 25}
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict)
mydict = thisdict.copy()
mydict["brand"]="Maruti"
print(mydict)







'''
print(car)
for x in car: 
 print(x)
for x in car:
 print(car[x])
'''


'''
dict = {
'emp1': {'name': 'Akash', 'salary': 15500},
'emp2': {'name': 'Ajay', 'salary': 18000},
'emp3': {'name': 'Vijay'}
}
dict['emp2']['salary'] = 15500
print(dict)
print(dict['emp3']['name'])
del dict['emp1']['salary']
print(dict)
'''





print(car.get('khushi','key not presnt'))



#greet('Parth') # function call 
# function definition
 



def my_function(x):
 a= 5 * x
 print("Inside Function",a)
my_function(3)
print(my_function(5))
print("Outside",my_function(9))
print("\n******")
def greet():#First define and than call
  print("Hello")
  return #Will go back to function call
  print("How are you")
greet() #Caling

#value ordered wrong
def result(name, marks): 
 print("Name of student : ", name,"marks is:",marks) 
result(95,'khushi')



def stud(course, sem, *papers):
  print("Course", course)
  print("Semester", sem)
  for p in papers:
    print("papers", p)
stud("BCA","Third",301,302,306, 308)


def my_function(**kid):
 print("His first name is " + kid["fname"]) #His first name is Ranbeer 
 print("His last name is " + kid["lname"]) #His last name is Kapoor
my_function(fname = "Ranbeer", lname = "Kapoor")

message="global"
def outer():
  message = 'local'
  print("outer:", message)
  def inner(): # nested function 
    nonlocal message 
    message='non local'
    print("inner:", message) 
  inner()#inner: Non Local
outer()#outer: Non Local
 
print("outer:", message) #outer:global


 







