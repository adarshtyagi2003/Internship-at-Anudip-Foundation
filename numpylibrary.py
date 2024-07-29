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


#to fetch digonal element or to update in the array

arr=np.array([[1,2,3],[4,5,6],[4,5,6]])
print(np.diag(arr))
print(np.diag((2,3,4)))

#random() function is used to create random number 


rand=np.random.randint(0,100,12)
print(rand)


#create an array 1 dimensional and convert it into another shape 

arr=np.random.randint(0,100,12)
print(arr)
arr=arr.reshape(4,3)
print(arr)
print("array value is:",arr[0][1])
print("array value is:",arr[1][0])
print(arr.shape)
arr=arr.reshape(-1,4)
print(arr)
arr=arr.reshape(2,-1)
print(arr)


#seed() function 
np.random.seed(145)
arr=np.random.randint(0,100,12)
print(arr)




#arange() function used to create array of sequence element

ar=np.arange(1,15)
print(ar)
print(ar[ar%2==0]) # to print all even numbers
print(ar[ar%2!=0]) # to print all odd numbers 

print(ar+2)
print(ar*2)
print(ar**2)



#various functions on array

arr=np.array([10,20,35,40,6,2])
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.sqrt(arr))
print(np.sin(arr))
print(np.cos(arr))



np.random.seed(122)
mat=np.random.randint(1,21,9).reshape(3,3)    
#mat.reshape(3,3)
print(mat)
print(np.sum(mat))
print(np.cumsum(mat))
print(np.min(mat))
print(np.max(mat))
print("---------------")
print(np.sum(mat,axis=0))
print(np.cumsum(mat,axis=0))
print(np.min(mat,axis=0))







np.random.seed (122)
mat =np.random.randint (1,21,10)
print (mat)
np.random.shuffle (mat)
print(mat)
print (np.unique (mat, return_index=True,return_counts=True))
print(np.unique(mat).size)



#transpose() function 

arr=np.array([[1,2,3],[4,5,6]])
transposed_arr=np.transpose(arr)
print("\n",transposed_arr)




#mean function 
arr=np.array([1,2,3,4,5])
print("\n",np.mean(arr))


#split function 

arr=np.array([1,4,6,7,8,2])
print("split array is:","\n",np.split(arr,3))



#sorted function 

arr=np.array([4,2,6,9,45,23,45,11])
print("sorted array is:","\n",np.sort(arr))

#to sort in descending order
arr=np.array([4,2,6,9,45,23,45,11])
print("sorted array in descending order:","\n",np.sort(arr)[::-1])



#to sort matrix row wise

matrix=np.array([[3,1,2],[6,5,4]])

sorted_matrix=np.sort(matrix,axis=1)
print("sorted array row wise:")
print(sorted_matrix)


#concatenate 2 array row wise 

arr1= np.array([[1,2],[3,4]])
arr2= np.array([[5,6],[7,8]])

result = np.concatenate((arr1,arr2),axis=1)
print("concatenate 2 arrays rowwise:",result)


#vstack() and hstack() function 

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])


result=np.vstack((arr1,arr2))
print("\n",result)

#hstack()

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
result=np.hstack((arr1,arr2))
print("\n",result)


#standard deviation,mean,variance

classA=np.array([85,88,90,92,95])
classA_mean=np.mean(classA)
print("\n",classA_mean)

variable=np.var(classA) #var() is a variance function
print(variable)

std=np.std(classA)
print(std)



