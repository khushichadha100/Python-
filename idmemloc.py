'''
X=10
print(id(X))
Y=20
z=X+Y
print(id(z))
#print(X+Y)  # 30 will be printed
X=30
print(id(X))
print(X+Y)
#X has a new value of 30 and Y has a value 20. Therefore, the result will be 50
Y=X
print(Y)
print(id(Y))
print(id(Y))
'''
A=10
print(A)
print(id(A)) 
B=20
print (B)
print(id(B))
A=B
print(A)
print(id(A))
print(id(B))