num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
num3=int(input("enter the number 3:"))

if(num1>num2 and num1>num3):
    print("num1 is largest",num1)
elif(num2>num1):
    print("num2 is largest",num2)
else:
    print(num3)        