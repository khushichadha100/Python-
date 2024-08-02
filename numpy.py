import numpy as np
#print(dir(np))
'''
arr = np.array([1, 2, 'a', 4,5,'b','c',8])
print(arr[::])
print(arr[2]+arr[3])
print(arr[1]+arr[4])
print(arr[2]+arr[4])
''' 
'''
print(arr[::2])
print(arr[::-1])
print(arr[0:8])
print(arr[0:9])
 
print(arr[4:])
print(arr[:4])




print(arr[-7:-1])
print(arr[-9:-4])
print(arr[-9:9])

print(arr[-8:5])
print(arr[-8:-4])



print(arr[-1])
print(arr[-2])
print(arr[-3])
print(arr[-4])
print(arr[-5])

#arr = np.array([[1, 2, 3], [4, 5, 6]])





arr = np.array([1, 'a', 3.3, [4,5],('ab',2,4,5),{'a':'apple',2:'banana'}])
print(arr)
print(arr[::])
print(arr[::2])
print(arr[::-1])
print(arr[0:4])
print(arr[0:5])
print(arr[-1:-4])




arr = np.array([1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14])

newarr = arr.reshape(2,7)
#newarr = arr.reshape(7, 2)

print(newarr)
newarr = arr.reshape(-1)

print(newarr)

'''
#arra=np.array(['b',2,3,4,5,6,'c',9])
arra1=np.array([1,2,3,4,5,6,7,8,9])
'''
print(min(arra))#works for string(2)
print(sum(arra))
print(max(arra))#works for string(c)
print(np.product(arra))
print(np.average(arra))
print(np.mean(arra))
print(np.median(arra))
 '''
#print(arra[3] - arra[4])
#arra=np.array(['b',2,3,4,5,6,'c',9])
#print(sum(arra))

#print(arra[4] - arra[3])
#print(arra[0]+arra[1])
#print(arra[0]-arra[6])

arra2=np.array([ 2,4,6,8,12,14,16,18,20])
'''
print(np.add(arra1,arra2))
print(np.subtract(arra1,arra2))
print(np.subtract(arra2,arra1))
print(np.multiply(arra1,arra2))
#print(np.divide(arra2,arra1))
'''
print(arra2.ndim)



