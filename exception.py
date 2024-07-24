print("line 1")
print("line 2")
print("line 3")
print("line 4")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try:
    result = num1 / num2                              #'''also can be done as  except(zerodivisionerror,filenotfounderror):'''
    print("The result of the division is:", result)   # print("something went wrong")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print("An unexpected error occurred:", e)

else:
    print("else block")
finally:
    print("finally block")
print("line 6")



#handle forcefull exception

def agecheck(age):
    if age>=18:
        print("you can vote")
    else:
        raise ValueError("you cannot vote")
    
try:
     agecheck(14)
except ValueError as e:
    print(e)