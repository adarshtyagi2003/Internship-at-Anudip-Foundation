#create a list of 20 numbers and print the element in backward direction using forward index

list=[]

for i in range(0,4):
    x=int(input("enter the number"))
    list.append(x)

#print(list[20:0:-1])     done by slicing 

#list.reverse()       done by reverse function
#print(list)

#can also be done as 

y=len(list)-1
for i in range(y,-1,-1):        #done using loop 
    print(list[i])