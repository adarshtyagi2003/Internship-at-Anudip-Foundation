x=100
count=0
while(x<1000):
    if(x%2==0 and x%3==0):
        count+=1
        print(x)
    x+=1
print(count)  
