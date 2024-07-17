cp=float(input("enter cost price(in Rs) : "))
sp=float(input("enter selling price(in Rs) : "))
if(cp<0):
    print("invalid cost price")
elif(sp<0):
    print("invalid selling price")
else:
    if(sp>cp):
      print("profit : Rs" ,(sp-cp))
    elif(cp>sp):
        print("loss : Rs" ,(cp-sp))
    else:
        print("no profit no loss")