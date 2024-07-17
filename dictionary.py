dict={"key":"value","stdid":"std101","name":"adarsh"}
print(dict)


#insert a element in a dictionary
dict["age"]=21
print(dict)


#print element using for loop 
for i in dict:
    print(i,"-",dict[i])


dict.pop("key")
print(dict)

dictobj1={'name':'amit','age':15,'standard':'10th'}
print(dictobj1)

dictobj2={'hindi':67,'age':16,'standard': '12th','english':67}
print(dictobj2)

#inserting all elements of second dictionary to dictionary first
dictobj1.update(dictobj2)
print(dictobj1)