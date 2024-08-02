 
'''
import sys # System files
a=sys.builtin_module_names # module names
print(a)
'''


#help('modules') 

 
import math as m

print(m.pi)
print('ceil is:',m.ceil(1.03))
print('ceil is:',m.ceil(-8.23))
print("\n******************")
print('ceil is:',m.ceil(1.63))
print('ceil is:',m.ceil(-8.63))
print("\n******************")
print('floor is:',m.floor(1.03))
print('floor is:',m.floor(-8.23))
print("\n******************")
print('floor is:',m.floor(1.63))
print('floor is:',m.floor(-8.63))
print("\n******************")
print('sqre is:',m.sqrt(36))
#print('expo is:',m.exp(3))
print('power is:',m.pow(2,5))
#print('sqre is:',m.sqrt(-4))#value error 
print("\n******************")
print(math.factorial(5))
import random
print(random.random())
