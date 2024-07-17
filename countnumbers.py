# count the numbers between 100 to 1000 which is even and divisible by 3.
print("these are the numbers that are even and divisible by 3 between 100 and 1000:")
count=0
for i in range(100,1000):
    if (i%2==0 and i%3==0):  
     count+=1
     print(i,end=' ')
print("\ntotal number that are even and divisible by 3 between 100 and 1000:" ,count)
        