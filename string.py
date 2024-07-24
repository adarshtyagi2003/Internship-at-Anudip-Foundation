name="adarsh"
print(name)

name=name+"Tyagi"
print(name)

# slicing
me ="I am a data analyst"
print("me[2:4]",me[2:4])
print("me[5:9]",me[5:9])
print("me[0:15]",me[:15])
print("me[:]",me[:])
print("me[::]",me[::])
print("me[0:17:3]",me[0:17:3])
print("me[::-1]",me[::-1])

#is operator

x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is z)
print(x is y)


#capitalize function 
str="adarsh tyagi"
str.capitalize()
print(str)
print(id(str))
str=str.capitalize()
print(str)


#center method() alligns string to the center by filling paddings left and right of the string.take 2 parameters,first is width
#second is fill character which is optional
str="adarsh"
print(str)
str=str.center(20,"*")
print(str)


#string count() method

str1="aa bbbbb aaaa cccc dddd eeee"
count=str1.count('b',0,len(str1))
print("count:",count)


#endswith()

str="welcome to python class"
issend=str.endswith("s")
print(issend)


#find 

str="i am a python developer"
str1=str.find("am")
print(str1)

#index 

str="i am adarsh tyagi"
str1=str.index("ad",0,len(str))
print(str1)


#isalnum() method

str="abcdefgh4567"
str1="hgyt fyt987"
print(str.isalnum())
print(str1.isalnum())


#isnumeric() method

str="467876875543"
str1=str.isnumeric()
print("all are numeric: ",str1)


#islower(),isupper()

str1="i am adarsh tyagi"
str2="i am a python developer"
print(str1.islower())
print(str2.isupper())


#lower(),upper()
str1="i am adarsh tyagi"
str2="I AM PYTHON DEVELOPER"
print(str1.upper())
print(str2.lower())




#lstrip(),rstrip()
#lstrip used to remove space from the left 
#rstrip used to remove space from the right 

str="     python     "
str2=str.lstrip()
print(str)
print(str2)
str3=str.rstrip()
print(str3)





