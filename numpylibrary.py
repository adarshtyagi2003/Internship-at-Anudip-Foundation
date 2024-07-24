import numpy as np

l=[10,30,25,45,78]
a=np.array(l)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]])

print("array:",a)
print("array:",b)
print("array:",c)
print("array:",d)



#to check the dimension of array
print("array dimension",a.ndim)
print("array dimension",b.ndim)
print("array dimension",c.ndim)
print("array dimension",d.ndim)


#slicing array in numpy 


arr=[10,20,30,4,5,6,7,8]
sarr=arr[1:5]
print(arr)
print(sarr)
sarr[3]=100
print(sarr)



#copy of array in numpy

array=[1,2,3,4,5]
arr=np.copy(array)
array[0]=42
print("original array:",array)
print("copy of array:",arr)



#zero() function
arr=np.zeros((6),dtype="int")
print("array of zeros:" ,arr)



#numpy ones() function in python is used to create an array of the specified shape and type

b=np.ones((6,2),dtype="int")
print(b)

c=np.ones((6,2),dtype="int")*10
print(c)



#eye() function is used to put element at diagonal 
arr=np.eye(4)
print("check element at diagonal:","\n",arr)

# diag() function is used to print different element at diagonal instead of 1 
arr1=np.diag([3,4,1,6])
print("check element at diagonal:","\n",arr1)