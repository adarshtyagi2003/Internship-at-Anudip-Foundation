# enter time in seconds and convert into hour,minutes and seconds

time= int(input("enter the time in seconds"))
if(time<60 and time>0):
  print(time)
if(time>60):
  hour=time//3600
  minutes=(time%3600)//60
  seconds=time%60
  print(hour, ":" ,minutes, ":", seconds)
