list=[23,45,98,67,54,87]

#insertion at end 
#append 
x=[23,45,22,21]
list.append(x)
print(list)
#extend function
y=[3,5,7,8]
list.extend(y)
print(list)

#insert element at specified position 
#insert function 

#syntax:- list.insert(index,element)
list.insert(4,69)
print(list)

#removing elements from list 

#pop method is used 
list.pop(2)
print(list)

#when we know the element and want to delete it then use remove function 
list.remove([23,45,22,21])
print(list)

#to clear all the element from list use clear method 
#clear function 

list.clear()
print(list)